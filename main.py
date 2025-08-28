"""
Options Trading Bot - Flattrade
Integration for FINNIFTY Implements specific options
strategy with trailing SL and re-entry logic
"""

import logging
import threading
import time
import json
import os
import sys
import math
from datetime import datetime, timedelta
import calendar
from typing import Dict, List, Any, Optional
import signal

# Local Imports
from auth import FlattradeAuth
from market_data import MarketDataManager
from risk_manager import RiskManager
from portfolio import PortfolioManager
from web_interface import WebInterface
from utils import setup_logging, load_config

# Configure logging
setup_logging({'logging': {'level': 'INFO'}})
logger = logging.getLogger(__name__)

class OptionsStrategyBot:
    """
    Options trading bot implementing specific strategy for FINNIFTY:
    - Buy 5th OTM CE, Sell 3rd OTM CE
    - Buy 5th OTM PE, Sell 3rd OTM PE
    - Lot size: 40 (FINNIFTY)
    - Start after 9:20 AM
    - Trailing SL with ₹300 profit threshold, ₹50 buffer, ₹1 trail
    - Re-entry after 5 mins if SL hit
    - Exit on SL hit or forcibly at 2:00 PM on expiry day
    """

    def __init__(self, config_file: str = 'config.json'):
        """Initialize the options trading bot"""
        self.config = load_config(config_file)
        self.running = False
        self.trading_enabled = True
        self.paper_trading = self.config.get('paper_trading', True)

        # Strategy parameters
        self.lot_size = 40  # FINNIFTY lot size
        self.start_time_hour = 9
        self.start_time_minute = 20
        self.profit_threshold = 300  # ₹300 profit to start trailing SL

