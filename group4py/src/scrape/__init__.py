"""
Scrape module for NDC document processing.

This module provides a clean interface for scraping, comparing, and updating
NDC documents from the UNFCCC registry.
"""

from .workflow import run_scraping_workflow
from .config import ScrapingConfig, DEFAULT_CONFIG
from .download import download_pdf

__all__ = [
    'run_scraping_workflow',
    'ScrapingConfig',
    'DEFAULT_CONFIG',
    'download_pdf'
] 