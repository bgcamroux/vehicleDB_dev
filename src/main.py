#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py"""

import os
import sys

import psycopg2
import pandas as pd
from configparser import ConfigParser

# The config file is located in the parent directory to this file.
configPath = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'config.ini')

config = ConfigParser()

if os.path.exists(configPath):
    print("Config Path: ", configPath)
    config.read(configPath)
else:
    print("Error: Configuration file 'config.ini' not found in parent directory.")
    sys.exit(1)
def main():
    db_config = {
        'host': config.get('database', 'host'),
        'port': config.get('database', 'port'),
        'database': config.get('database', 'database'),
        'user': config.get('database', 'user'),
        'password': config.get('database', 'password')
    }
    
    print(db_config)

if __name__ == "__main__":
    main()
