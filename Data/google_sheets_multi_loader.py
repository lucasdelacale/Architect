"""
Google Sheets Multi-Sheet Loader
Integração com múltiplas abas de uma planilha Google Sheets pública.

Este módulo fornece funções para carregar dados de performance (D-1)
e dados de controle por plataforma de mídia digital.

Versão: 3.0 - Adicionado tratamento de linha de total da plataforma.
"""

import json
import logging
import time
from pathlib import Path
from typing import Dict, Optional, Tuple, Any, Union
import pandas as pd
import requests
from io import StringIO

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SheetCache:
    """
    Cache para dados do Google Sheets com suporte a TTL e persistência em disco.
    
    Attributes:
        ttl: Tempo de vida do cache em segundos (padrão: 300 = 5 minutos)
        cache: Dicionário com os dados em cache
        timestamps: Dicionário com timestamps de cada entrada
        request_count: Contador de requisições feitas
        cache_dir: Diretório para cache em disco
    """
    
    def __init__(self, ttl_seconds: int = 300, cache_dir: Optional[Union[str, Path]] = None):
        """
        Inicializa o cache.
        
        Args:
            ttl_seconds: Tempo de vida do cache em segundos (padrão: 300 = 5 minutos)
            cache_dir: Diretório para cache em disco (opcional)
        """
        self.ttl = ttl_seconds
        self.cache: Dict[str, pd.DataFrame] = {}
        self.timestamps: Dict[str, float] = {}
        self.request_count = 0
        self.total_requests = 0
        self.cache_hits = 0
        self.cache_misses = 0
        
        # Configurar diretório de cache em disco
        if cache_dir:
            self.cache_dir = Path(cache_dir)
        else:
            # Usar diretório padrão relativo ao script
            self.cache_dir = Path(__file__).parent / "cache"
        
        # Criar diretório se não existir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Cache inicializado com TTL de {ttl_seconds}s e diretório: {self.cache_dir}")
    
    def get(self, key: str) -> Optional[pd.DataFrame]:
        """
        Recupera dados do cache se válidos.
        
        Args:
            key: Chave do cache
            
        Returns:
            DataFrame se encontrado e válido, None caso contrário
        """
        self.total_requests += 1
        
        if key in self.cache:
            if time.time() - self.timestamps[key] < self.ttl:
                self.cache_hits += 1
                logger.debug(f"Cache hit para chave: {key}")
                return self.cache[key]
            else:
                # Cache expirado
                self.invalidate(key)
                logger.debug(f"Cache expirado para chave: {key}")
        
        self.cache_misses += 1
        logger.debug(f"Cache miss para chave: {key}")
        return None
    
    def set(self, key: str, value: pd.DataFrame) -> None:
        """
        Armazena dados no cache.
        
        Args:
            key: Chave do cache
            value: DataFrame para armazenar
        """
        self.cache[key] = value
        self.timestamps[key] = time.time()
        self.request_count += 1
        
        # Salvar em disco também
        self._save_to_disk(key, value)
        
        logger.debug(f"Dados armazenados no cache: {key}")
    
    def invalidate(self, key: Optional[str] = None) -> None:
        """
        Invalida entradas do cache.
        
        Args:
            key: Chave específica para invalidar (None para invalidar tudo)
        """
        if key:
            self.cache.pop(key, None)
            self.timestamps.pop(key, None)
            # Remover do disco
            cache_file = self.cache_dir / f"{key}.json"
            if cache_file.exists():
                cache_file.unlink()
                logger.debug(f"Cache removido do disco: {key}")
        else:
            self.cache.clear()
            self.timestamps.clear()
            # Limpar todos os arquivos do disco
            for cache_file in self.cache_dir.glob("*.json"):
                cache_file.unlink()
            logger.debug("Cache completamente invalidado")
    
    def _save_to_disk(self, key: str, value: pd.DataFrame) -> None:
        """
        Salva DataFrame em cache no disco.
        
        Args:
            key: Chave do cache
            value: DataFrame para salvar
        """
        try:
            # Limpar caracteres especiais do nome do arquivo
            safe_key = "".join(c for c in key if c.isalnum() or c in ('-', '_')).strip()
            cache_file = self.cache_dir / f"{safe_key}.json"
            data = {
                'data': value.to_json(orient='records', date_format='iso'),
                'columns': value.columns.tolist(),
                'timestamp': self.timestamps.get(key, time.time())
            }
            
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            logger.debug(f"Dados salvos em disco: {cache_file}")
        except Exception as e:
            logger.warning(f"Erro ao salvar cache em disco: {e}")
    
    def _load_from_disk(self, key: str) -> Optional[pd.DataFrame]:
        """
        Carrega DataFrame do cache em disco.
        
        Args:
            key: Chave do cache
            
        Returns:
            DataFrame se encontrado, None caso contrário
        """
        try:
            cache_file = self.cache_dir / f"{key}.json"
            
            if not cache_file.exists():
                return None
            
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Verificar se não expirou
            if time.time() - data.get('timestamp', 0) >= self.ttl:
                cache_file.unlink()
                return None
            
            # Reconstruir DataFrame
            df = pd.read_json(data['data'], orient='records')
            
            # Restaurar colunas se necessário
            if 'columns' in data and list(df.columns) != data['columns']:
                df.columns = data['columns']
            
            logger.debug(f"Dados carregados do disco: {cache_file}")
            return df
            
        except Exception as e:
            logger.warning(f"Erro ao carregar cache do disco: {e}")
            return None
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Retorna métricas do cache.
        
        Returns:
            Dicionário com métricas de performance
        """
        hit_rate = (self.cache_hits / self.total_requests * 100) if self.total_requests > 0 else 0
        
        # Calcular tamanho do cache em bytes
        cache_size_mb = 0
        for cache_file in self.cache_dir.glob("*.json"):
            cache_size_mb += cache_file.stat().st_size / (1024 * 1024)
        
        return {
            'cache_size_entries': len(self.cache),
            'cache_size_mb': round(cache_size_mb, 2),
            'request_count': self.request_count,
            'total_requests': self.total_requests,
            'cache_hits': self.cache_hits,
            'cache_misses': self.cache_misses,
            'hit_rate_percent': round(hit_rate, 2),
            'ttl_seconds': self.ttl
        }
    
    def clear_metrics(self) -> None:
        """Limpa métricas de performance."""
        self.request_count = 0
        self.total_requests = 0
        self.cache_hits = 0
        self.cache_misses = 0


# Instância global do cache
_cache = SheetCache(ttl_seconds=300)

# Constantes
SPREADSHEET_ID = "1qJn7qBhEmKV5wbsqrDQ-9o5WKQZ2x5EcZNanDNDwzM4"
BASE_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}"

# Mapeamento de plataformas para GIDs (precisam ser preenchidos com os GIDs reais)
# Estes são exemplos - os GIDs reais precisam ser obtidos da planilha
PLATFORM_GIDS = {
    "database": "0",  # GID da aba Database (dados D-1)
    "google": "0",    # GID da aba Google Ads | NET
    "dv360": "0",     # GID da aba DV360 | NET
    "facebook": "0",  # GID da aba FACEBOOK Ads| NET
    "tiktok": "0",    # GID da aba TIKTOK Ads| NET
    "bing": "0",      # GID da aba BING Ads| NET
}

# Nomes das abas na planilha (para fallback por nome)
PLATFORM_SHEET_NAMES = {
    "database": "Database",
    "google": "Google Ads | NET",
    "dv360": "DV360 | NET",
    "facebook": "FACEBOOK Ads| NET",
    "tiktok": "TIKTOK Ads| NET",
    "bing": "BING Ads| NET",
}

# Colunas esperadas para dados D-1
D1_COLUMNS = [
    "date", "id", "tx_vehicle", "tx_funnel", "Investimento", 
    "Impressoes", "Cliques", "Sessoes_GA4", "Sessoes_App", 
    "sessoes_totais", "conversoes_app", "conversoes_ga4", 
    "conversoes_totais", "instalacoes"
]

# Colunas esperadas para dados de controle (baseado na estrutura real da planilha)
CONTROL_COLUMNS = [
    "Campanha", "Funil", "Tipo", "Nº", "Audiência", "Projetado", "Custo", 
    "Sobra", "Consumo ontem", "Investimento Diarizado", "Pacing", "MTD", 
    "% Desvio Consumo X planejado", "Diarizado ajustado", "Linear", 
    "Diferença Plan X Realizado", " compensado", "CPA", "Conv.", "CPA Plan", "Conversões Plan"
]

# Mapeamento de colunas para nomes padronizados
COLUMN_MAPPING = {
    "Nº": "Nº",
    "Conv.": "Conv.",
    "Conversões Plan": "Conversões Plan",
    "Audiência": "Audiência",
    "Consumo ontem": "Consumo ontem",
    "Consumo  ontem": "Consumo ontem",
    "Investimento Diarizado": "Investimento Diarizado",
    "Investimento  Diarizado": "Investimento Diarizado",
    "% Desvio Consumo X planejado": "% Desvio Consumo X planejado",
    "% Desvio  Consumo X  planejado": "% Desvio Consumo X planejado",
    "Diferença Plan X Realizado": "Diferença Plan X Realizado",
    "Diferen\u00e7a Plan X Realizado": "Diferença Plan X Realizado",
    " compensado": "compensado",
    " \ncompensado": "compensado",
    "compensado": "compensado",
}


def _build_csv_url(gid: str = "0", sheet_name: Optional[str] = None) -> str:
    """
    Constrói URL para exportação CSV da planilha.
    
    Args:
        gid: GID da aba (padrão: "0" para primeira aba)
        sheet_name: Nome da aba (alternativa ao gid)
    
    Returns:
        URL formatada para exportação CSV
    """
    if sheet_name:
        # Usar nome da aba (funciona para planilhas públicas)
        encoded_name = requests.utils.quote(sheet_name)
        return f"{BASE_URL}/gviz/tq?tqx=out:csv&sheet={encoded_name}"
    else:
        # Usar GID
        return f"{BASE_URL}/gviz/tq?tqx=out:csv&gid={gid}"


def _load_sheet_to_dataframe(
    gid: str = "0", 
    sheet_name: Optional[str] = None,
    columns: Optional[list] = None,
    use_cache: bool = True
) -> pd.DataFrame:
    """
    Carrega uma aba específica para DataFrame com suporte a cache.
    
    Args:
        gid: GID da aba
        sheet_name: Nome da aba (alternativa ao gid)
        columns: Lista de colunas esperadas para validação
        use_cache: Se deve usar cache (padrão: True)
    
    Returns:
        DataFrame com os dados da aba
    
    Raises:
        requests.exceptions.RequestException: Erro de conexão
        pd.errors.EmptyDataError: Planilha vazia
        ValueError: Estrutura de dados inesperada
    """
    # Gerar chave do cache
    cache_key = f"sheet_{gid}_{sheet_name or 'default'}"
    
    # Verificar cache se habilitado
    if use_cache:
        cached_data = _cache.get(cache_key)
        if cached_data is not None:
            logger.info(f"Usando dados em cache para: {sheet_name or gid}")
            return cached_data
    
    url = _build_csv_url(gid, sheet_name)
    logger.info(f"Carregando dados de: {url[:80]}...")
    
    try:
        start_time = time.time()
        response = requests.get(url, timeout=60)
        response.raise_for_status()
        
        # Verificar se o conteúdo é CSV válido
        if not response.text.strip():
            raise pd.errors.EmptyDataError("Planilha retornou vazia")
        
        # Carregar CSV para DataFrame
        df = pd.read_csv(StringIO(response.text))
        
        # Limpar nomes das colunas (remover espaços extras e quebras de linha)
        df.columns = [col.strip().replace('\n', ' ') for col in df.columns]
        
        # Padronizar nomes das colunas conforme mapeamento
        df.rename(columns=COLUMN_MAPPING, inplace=True)
        
        # Validar estrutura se colunas esperadas fornecidas
        if columns:
            missing_cols = [col for col in columns if col not in df.columns]
            if missing_cols:
                logger.warning(f"Colunas faltando: {missing_cols}")
                # Não levantar erro, apenas logar aviso
        
        # Armazenar no cache se habilitado
        if use_cache:
            _cache.set(cache_key, df)
        
        response_time = time.time() - start_time
        logger.info(f"Carregadas {len(df)} linhas com {len(df.columns)} colunas em {response_time:.2f}s")
        return df
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro de conexão ao acessar planilha: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        logger.error(f"Dados vazios: {e}")
        raise
    except Exception as e:
        logger.error(f"Erro inesperado ao carregar planilha: {e}")
        raise


def load_d1_data(use_cache: bool = True) -> pd.DataFrame:
    """
    Carrega dados D-1 (performance) da aba Database.
    
    Args:
        use_cache: Se deve usar cache (padrão: True)
    
    Returns:
        DataFrame com dados de performance diária
    """
    logger.info("Carregando dados D-1 (performance)...")
    
    # Tentar primeiro com GID, depois com nome da aba
    try:
        return _load_sheet_to_dataframe(
            gid=PLATFORM_GIDS["database"],
            columns=D1_COLUMNS,
            use_cache=use_cache
        )
    except Exception as e:
        logger.warning(f"Falha com GID, tentando com nome da aba: {e}")
        return _load_sheet_to_dataframe(
            sheet_name=PLATFORM_SHEET_NAMES["database"],
            columns=D1_COLUMNS,
            use_cache=use_cache
        )


def load_platform_control(platform_name: str, use_cache: bool = True) -> pd.DataFrame:
    """
    Carrega dados de controle de uma plataforma específica, excluindo a linha de total.
    
    A linha 2 (após cabeçalho) é sempre o total da plataforma e será marcada
    com flag `is_total=True`. Esta função retorna apenas as campanhas individuais.
    
    Args:
        platform_name: Nome da plataforma (google, dv360, facebook, tiktok, bing)
        use_cache: Se deve usar cache (padrão: True)
    
    Returns:
        DataFrame com dados de controle das campanhas individuais (exclui linha de total)
    """
    platform_lower = platform_name.lower()
    
    if platform_lower not in PLATFORM_GIDS:
        raise ValueError(
            f"Plataforma '{platform_name}' não reconhecida. "
            f"Opções: {list(PLATFORM_GIDS.keys())}"
        )
    
    logger.info(f"Carregando dados de controle da plataforma: {platform_name}")
    
    # Tentar primeiro com nome da aba (mais confiável)
    try:
        df = _load_sheet_to_dataframe(
            sheet_name=PLATFORM_SHEET_NAMES[platform_lower],
            columns=CONTROL_COLUMNS,
            use_cache=use_cache
        )
        
        # Verificar se as colunas esperadas estão presentes
        expected_cols = ["Campanha", "Funil", "Nº", "Projetado", "CPA Plan", "Conversões Plan"]
        missing_cols = [col for col in expected_cols if col not in df.columns]
        
        if missing_cols:
            logger.warning(f"Colunas de controle faltando: {missing_cols}")
            # Tentar com GID como fallback
            logger.info("Tentando com GID como fallback...")
            df = _load_sheet_to_dataframe(
                gid=PLATFORM_GIDS[platform_lower],
                columns=CONTROL_COLUMNS,
                use_cache=use_cache
            )
        
        # Separar linha de total das campanhas individuais
        # A linha 2 (índice 0) é sempre o total da plataforma
        if len(df) > 1:
            logger.info(f"Identificada linha de total na plataforma {platform_name}")
            # Marcar linha de total
            df['is_total'] = False
            df.iloc[0, df.columns.get_loc('is_total')] = True
            
            # Retornar apenas campanhas individuais (excluindo linha de total)
            campaign_details = df.iloc[1:].copy()
            logger.info(f"Retornando {len(campaign_details)} campanhas individuais")
            return campaign_details
        
        # Se houver apenas uma linha, retornar como está (sem flag de total)
        logger.warning(f"Plataforma {platform_name} possui apenas uma linha de dados")
        return df
        
    except Exception as e:
        logger.warning(f"Falha com nome da aba, tentando com GID: {e}")
        df = _load_sheet_to_dataframe(
            gid=PLATFORM_GIDS[platform_lower],
            columns=CONTROL_COLUMNS,
            use_cache=use_cache
        )
        
        # Separar linha de total das campanhas individuais
        if len(df) > 1:
            logger.info(f"Identificada linha de total na plataforma {platform_name}")
            df['is_total'] = False
            df.iloc[0, df.columns.get_loc('is_total')] = True
            
            campaign_details = df.iloc[1:].copy()
            logger.info(f"Retornando {len(campaign_details)} campanhas individuais")
            return campaign_details
        
        return df


def load_platform_totals(platform_name: str, use_cache: bool = True) -> pd.DataFrame:
    """
    Retorna DataFrame com apenas o total da plataforma.
    
    A linha 2 (após cabeçalho) é sempre o total da plataforma e será marcada
    com flag `is_total=True`.
    
    Args:
        platform_name: Nome da plataforma (google, dv360, facebook, tiktok, bing)
        use_cache: Se deve usar cache (padrão: True)
    
    Returns:
        DataFrame com apenas a linha de total da plataforma
    """
    platform_lower = platform_name.lower()
    
    if platform_lower not in PLATFORM_GIDS:
        raise ValueError(
            f"Plataforma '{platform_name}' não reconhecida. "
            f"Opções: {list(PLATFORM_GIDS.keys())}"
        )
    
    logger.info(f"Carregando totais da plataforma: {platform_name}")
    
    # Tentar primeiro com nome da aba (mais confiável)
    try:
        df = _load_sheet_to_dataframe(
            sheet_name=PLATFORM_SHEET_NAMES[platform_lower],
            columns=CONTROL_COLUMNS,
            use_cache=use_cache
        )
        
        # Verificar se as colunas esperadas estão presentes
        expected_cols = ["Campanha", "Funil", "Nº", "Projetado", "CPA Plan", "Conversões Plan"]
        missing_cols = [col for col in expected_cols if col not in df.columns]
        
        if missing_cols:
            logger.warning(f"Colunas de controle faltando: {missing_cols}")
            # Tentar com GID como fallback
            logger.info("Tentando com GID como fallback...")
            df = _load_sheet_to_dataframe(
                gid=PLATFORM_GIDS[platform_lower],
                columns=CONTROL_COLUMNS,
                use_cache=use_cache
            )
        
        # Extrair linha de total (índice 0)
        if len(df) > 1:
            logger.info(f"Extraindo linha de total da plataforma {platform_name}")
            platform_totals = df.iloc[0:1].copy()
            platform_totals['is_total'] = True
            logger.info(f"Total da plataforma extraído com sucesso")
            return platform_totals
        
        # Se houver apenas uma linha, retornar como está
        logger.warning(f"Plataforma {platform_name} possui apenas uma linha de dados")
        df['is_total'] = True
        return df
        
    except Exception as e:
        logger.warning(f"Falha com nome da aba, tentando com GID: {e}")
        df = _load_sheet_to_dataframe(
            gid=PLATFORM_GIDS[platform_lower],
            columns=CONTROL_COLUMNS,
            use_cache=use_cache
        )
        
        # Extrair linha de total
        if len(df) > 1:
            logger.info(f"Extraindo linha de total da plataforma {platform_name}")
            platform_totals = df.iloc[0:1].copy()
            platform_totals['is_total'] = True
            return platform_totals
        
        df['is_total'] = True
        return df


def get_platform_summary(platform_name: str, use_cache: bool = True) -> Dict[str, Any]:
    """
    Retorna resumo completo: total + campanhas.
    
    Args:
        platform_name: Nome da plataforma (google, dv360, facebook, tiktok, bing)
        use_cache: Se deve usar cache (padrão: True)
    
    Returns:
        Dicionário com:
        - totals: DataFrame com total da plataforma
        - campaigns: DataFrame com campanhas individuais
        - campaign_count: Número de campanhas
    """
    logger.info(f"Gerando resumo completo da plataforma: {platform_name}")
    
    totals = load_platform_totals(platform_name, use_cache)
    campaigns = load_platform_control(platform_name, use_cache)
    
    return {
        'totals': totals,
        'campaigns': campaigns,
        'campaign_count': len(campaigns)
    }


def calculate_platform_metrics(platform_name: str, use_cache: bool = True) -> Dict[str, Any]:
    """
    Calcula métricas da plataforma usando totais corretos.
    
    Métricas que são SOMA (acumulado):
    - Projetado, Custo, Sobra, Consumo ontem, Investimento Diarizado,
    - MTD, Linear, Diferença Plan X Realizado, Compensado, Conv., Conversões Plan
    
    Métricas que são MÉDIA:
    - Pacing (%), % Desvio Consumo X planejado, CPA, CPA Plan
    
    Args:
        platform_name: Nome da plataforma (google, dv360, facebook, tiktok, bing)
        use_cache: Se deve usar cache (padrão: True)
    
    Returns:
        Dicionário com métricas calculadas corretamente
    """
    logger.info(f"Calculando métricas da plataforma: {platform_name}")
    
    totals = load_platform_totals(platform_name, use_cache).iloc[0]
    campaigns = load_platform_control(platform_name, use_cache)
    
    # Função auxiliar para converter valores brasileiros para float
    def parse_brazilian_currency(value, default=0):
        """Converte valores como 'R$ 2.547.460,45' para float."""
        if pd.isna(value):
            return default
        
        if isinstance(value, (int, float)):
            return float(value)
        
        if isinstance(value, str):
            # Remover R$, espaços e pontos (separador de milhar)
            # Substituir vírgula por ponto (separador decimal)
            cleaned = value.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')
            try:
                return float(cleaned)
            except ValueError:
                return default
        
        return default
    
    def parse_percentage(value, default=0):
        """Converte valores como '27,38%' para float."""
        if pd.isna(value):
            return default
        
        if isinstance(value, (int, float)):
            return float(value)
        
        if isinstance(value, str):
            # Remover % e espaços
            cleaned = value.replace('%', '').replace(' ', '').replace(',', '.')
            try:
                return float(cleaned)
            except ValueError:
                return default
        
        return default
    
    def to_float(value, default=0):
        """Tenta converter para float, tratando valores brasileiros."""
        try:
            if pd.isna(value):
                return default
            return float(value)
        except (ValueError, TypeError):
            return default
    
    # Métricas de soma (já estão nos totais)
    investimento_total = parse_brazilian_currency(totals.get('Projetado', 0))
    custo_total = parse_brazilian_currency(totals.get('Custo', 0))
    sobra_total = parse_brazilian_currency(totals.get('Sobra', 0))
    consumo_ontem_total = parse_brazilian_currency(totals.get('Consumo ontem', 0))
    investimento_diarizado_total = parse_brazilian_currency(totals.get('Investimento Diarizado', 0))
    mtd_total = parse_brazilian_currency(totals.get('MTD', 0))
    linear_total = parse_brazilian_currency(totals.get('Linear', 0))
    diferenca_plan_realizado = parse_brazilian_currency(totals.get('Diferença Plan X Realizado', 0))
    compensado_total = parse_brazilian_currency(totals.get('compensado', 0))
    
    # Para conversões, tratar formato brasileiro (6.168 = 6168)
    def parse_conversions(value, default=0):
        """Converte valores como '6.168' para 6168."""
        if pd.isna(value):
            return default
        
        if isinstance(value, (int, float)):
            return float(value)
        
        if isinstance(value, str):
            # Se contém ponto e vírgula, é formato brasileiro
            if '.' in value and ',' in value:
                # Ex: 1.234,56 -> 1234.56
                cleaned = value.replace('.', '').replace(',', '.')
            elif '.' in value:
                # Pode ser 6.168 (6168) ou 6.168 (6.168)
                # Se após o ponto há apenas 3 dígitos, é separador de milhar
                parts = value.split('.')
                if len(parts) == 2 and len(parts[1]) == 3:
                    # Formato: 6.168 (6168)
                    cleaned = value.replace('.', '')
                else:
                    # Formato: 6.168 (6.168)
                    cleaned = value
            elif ',' in value:
                # Formato: 6,168 (6.168)
                cleaned = value.replace(',', '.')
            else:
                cleaned = value
            
            try:
                return float(cleaned)
            except ValueError:
                return default
        
        return default
    
    conv_total = parse_conversions(totals.get('Conv.', 0))
    conv_plan_total = parse_conversions(totals.get('Conversões Plan', 0))
    
    # Métricas de média (calcular das campanhas)
    # Converter colunas para numérico antes de calcular média
    pacing_medio = 0
    desvio_medio = 0
    cpa_medio = 0
    cpa_plan_medio = 0
    
    if 'Pacing' in campaigns.columns:
        pacing_numeric = campaigns['Pacing'].apply(lambda x: parse_percentage(x))
        pacing_medio = pacing_numeric.mean() if not pacing_numeric.isna().all() else 0
    
    if '% Desvio Consumo X planejado' in campaigns.columns:
        desvio_numeric = campaigns['% Desvio Consumo X planejado'].apply(lambda x: parse_percentage(x))
        desvio_medio = desvio_numeric.mean() if not desvio_numeric.isna().all() else 0
    
    if 'CPA' in campaigns.columns:
        cpa_numeric = campaigns['CPA'].apply(lambda x: parse_brazilian_currency(x))
        cpa_medio = cpa_numeric.mean() if not cpa_numeric.isna().all() else 0
    
    if 'CPA Plan' in campaigns.columns:
        cpa_plan_numeric = campaigns['CPA Plan'].apply(lambda x: parse_brazilian_currency(x))
        cpa_plan_medio = cpa_plan_numeric.mean() if not cpa_plan_numeric.isna().all() else 0
    
    # Métricas derivadas
    desvio_total = ((custo_total - investimento_total) / investimento_total * 100) if investimento_total > 0 else 0
    roi_plan = conv_plan_total / investimento_total if investimento_total > 0 else 0
    roi_real = conv_total / custo_total if custo_total > 0 else 0
    
    return {
        'investimento_projetado': investimento_total,
        'investimento_realizado': custo_total,
        'sobra': sobra_total,
        'consumo_ontem': consumo_ontem_total,
        'investimento_diarizado': investimento_diarizado_total,
        'mtd': mtd_total,
        'linear': linear_total,
        'diferenca_plan_realizado': diferenca_plan_realizado,
        'compensado': compensado_total,
        'conversoes_realizadas': conv_total,
        'conversoes_planejadas': conv_plan_total,
        'pacing_medio': pacing_medio,
        'desvio_medio': desvio_medio,
        'cpa_medio': cpa_medio,
        'cpa_plan_medio': cpa_plan_medio,
        'desvio_percentual': desvio_total,
        'roi_planejado': roi_plan,
        'roi_realizado': roi_real
    }


def load_all_sheets_data(use_cache: bool = True) -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]:
    """
    Carrega todos os dados da planilha: D-1 e controle por plataforma.
    
    Args:
        use_cache: Se deve usar cache (padrão: True)
    
    Returns:
        Tupla com:
        - DataFrame com dados D-1 (performance)
        - Dicionário com DataFrames por plataforma (controle)
    """
    logger.info("Carregando todos os dados da planilha...")
    
    # Carregar dados D-1
    d1_data = load_d1_data(use_cache=use_cache)
    
    # Carregar dados de controle por plataforma
    control_data = {}
    platforms = ["google", "dv360", "facebook", "tiktok", "bing"]
    
    for platform in platforms:
        try:
            control_data[platform] = load_platform_control(platform, use_cache=use_cache)
            logger.info(f"Dados de controle carregados: {platform}")
        except Exception as e:
            logger.error(f"Erro ao carregar dados de {platform}: {e}")
            # Criar DataFrame vazio em caso de erro
            control_data[platform] = pd.DataFrame(columns=CONTROL_COLUMNS)
    
    logger.info(f"Todos os dados carregados com sucesso")
    return d1_data, control_data


def get_campaign_benchmarks(campaign_id: str, use_cache: bool = True) -> Dict[str, Any]:
    """
    Busca benchmarks de uma campanha específica em todas as plataformas.
    
    Args:
        campaign_id: ID da campanha (coluna 'Nº' na planilha)
        use_cache: Se deve usar cache (padrão: True)
    
    Returns:
        Dicionário com benchmarks encontrados:
        {
            'campaign_id': str,
            'platform': str,
            'campanha': str,
            'funil': str,
            'projetado': float,
            'cpa_plan': float,
            'conv_plan': float,
            'found_in': list  # Lista de plataformas onde foi encontrado
        }
    """
    logger.info(f"Buscando benchmarks para campanha: {campaign_id}")
    
    # Carregar todos os dados de controle
    _, control_data = load_all_sheets_data(use_cache=use_cache)
    
    benchmarks = {
        'campaign_id': campaign_id,
        'platform': None,
        'campanha': None,
        'funil': None,
        'projetado': None,
        'cpa_plan': None,
        'conv_plan': None,
        'found_in': []
    }
    
    # Buscar em cada plataforma
    for platform, df in control_data.items():
        if df.empty:
            continue
        
        # Normalizar nome da coluna do ID
        id_col = 'Nº' if 'Nº' in df.columns else 'N°'
        
        if id_col not in df.columns:
            logger.warning(f"Coluna de ID não encontrada na plataforma {platform}")
            continue
        
        # Converter ID para string para comparação
        df[id_col] = df[id_col].astype(str)
        
        # Buscar campanha
        match = df[df[id_col] == str(campaign_id)]
        
        if not match.empty:
            row = match.iloc[0]
            benchmarks['found_in'].append(platform)
            
            # Preencher dados (priorizar plataforma mais específica)
            if benchmarks['platform'] is None:
                benchmarks['platform'] = platform
                benchmarks['campanha'] = row.get('Campanha')
                benchmarks['funil'] = row.get('Funil')
                benchmarks['projetado'] = row.get('Projetado')
                benchmarks['cpa_plan'] = row.get('CPA Plan')
                benchmarks['conv_plan'] = row.get('Conversões Plan')
    
    if not benchmarks['found_in']:
        logger.warning(f"Campanha {campaign_id} não encontrada em nenhuma plataforma")
    
    return benchmarks


def refresh_data(platform_name: Optional[str] = None) -> Union[pd.DataFrame, Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]]:
    """
    Força refresh de dados, ignorando cache.
    
    Args:
        platform_name: Nome da plataforma específica (None para todas)
    
    Returns:
        DataFrame se platform_name especificado, ou tupla com todos os dados
    """
    logger.info(f"Forçando refresh de dados{f' para {platform_name}' if platform_name else ''}")
    
    if platform_name:
        # Refresh de plataforma específica
        return load_platform_control(platform_name, use_cache=False)
    else:
        # Refresh de todos os dados
        return load_all_sheets_data(use_cache=False)


def refresh_all_data() -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame]]:
    """
    Força refresh de todos os dados (invalida cache).
    
    Returns:
        Tupla com todos os dados atualizados
    """
    _cache.invalidate()
    logger.info("Cache invalidado - próxima requisição buscará dados atualizados")
    return load_all_sheets_data(use_cache=False)


def get_cache_metrics() -> Dict[str, Any]:
    """
    Retorna métricas do cache.
    
    Returns:
        Dicionário com métricas de performance
    """
    return _cache.get_metrics()


def clear_cache_metrics() -> None:
    """Limpa métricas do cache."""
    _cache.clear_metrics()


def set_cache_ttl(ttl_seconds: int) -> None:
    """
    Configura o TTL do cache.
    
    Args:
        ttl_seconds: Novo tempo de vida em segundos
    """
    _cache.ttl = ttl_seconds
    logger.info(f"TTL do cache atualizado para {ttl_seconds}s")


def test_connection() -> bool:
    """
    Testa a conexão com a planilha Google Sheets.
    
    Returns:
        True se conexão bem-sucedida, False caso contrário
    """
    try:
        logger.info("Testando conexão com Google Sheets...")
        
        # Testar com a aba Database
        url = _build_csv_url(gid=PLATFORM_GIDS["database"])
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Verificar se retornou dados
        if response.text.strip():
            logger.info("Conexão bem-sucedida!")
            return True
        else:
            logger.error("Planilha retornou vazia")
            return False
            
    except Exception as e:
        logger.error(f"Falha na conexão: {e}")
        return False


if __name__ == "__main__":
    # Exemplo de uso
    print("=== Teste de Integração Google Sheets Multi-Sheet ===\n")
    
    # Testar conexão
    if test_connection():
        print("✓ Conexão estabelecida com sucesso\n")
        
        # Carregar dados D-1
        print("Carregando dados D-1...")
        d1_data = load_d1_data()
        print(f"✓ Dados D-1: {len(d1_data)} linhas, {len(d1_data.columns)} colunas\n")
        
        # Carregar dados de controle
        print("Carregando dados de controle...")
        d1, control_data = load_all_sheets_data()
        
        for platform, df in control_data.items():
            print(f"  ✓ {platform}: {len(df)} linhas")
        
        # Mostrar métricas do cache
        print("\n=== Métricas do Cache ===")
        metrics = get_cache_metrics()
        print(f"  Entradas no cache: {metrics['cache_size_entries']}")
        print(f"  Tamanho do cache: {metrics['cache_size_mb']} MB")
        print(f"  Total de requisições: {metrics['total_requests']}")
        print(f"  Cache hits: {metrics['cache_hits']}")
        print(f"  Taxa de acerto: {metrics['hit_rate_percent']}%")
        
        print("\n=== Exemplo de Benchmarks ===")
        
        # Buscar benchmarks de uma campanha específica
        # Nota: Use um ID de campanha real da sua planilha
        example_id = "467"  # Substitua por um ID real
        benchmarks = get_campaign_benchmarks(example_id)
        
        if benchmarks['found_in']:
            print(f"\nCampanha {example_id} encontrada em: {', '.join(benchmarks['found_in'])}")
            print(f"  Nome: {benchmarks['campanha']}")
            print(f"  Funil: {benchmarks['funil']}")
            print(f"  Projetado: {benchmarks['projetado']}")
            print(f"  CPA Plan: {benchmarks['cpa_plan']}")
            print(f"  Conversões Plan: {benchmarks['conv_plan']}")
        else:
            print(f"\nCampanha {example_id} não encontrada")
        
        # Exemplo de refresh
        print("\n=== Exemplo de Refresh ===")
        print("Executando refresh de dados...")
        refresh_all_data()
        print("✓ Dados atualizados com sucesso")
        
        # Mostrar métricas atualizadas
        print("\n=== Métricas Atualizadas ===")
        metrics = get_cache_metrics()
        print(f"  Total de requisições: {metrics['total_requests']}")
        print(f"  Cache hits: {metrics['cache_hits']}")
            
    else:
        print("✗ Falha na conexão")
        print("Verifique se a planilha está pública e acessível")