# Architect Data Module
# Módulo de dados do Architect

from .google_sheets_multi_loader import (
    load_all_sheets_data,
    load_d1_data,
    load_platform_control,
    get_campaign_benchmarks,
    test_connection,
)

__all__ = [
    "load_all_sheets_data",
    "load_d1_data",
    "load_platform_control",
    "get_campaign_benchmarks",
    "test_connection",
]