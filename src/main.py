#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py"""

import os
import sys

# import psycopg2
# import pandas as pd
# from configparser import ConfigParser
 
from db.db_config import read_dbConfig as readConfig
from db.db_config import dbConnection

def main():
    print("Attempt DB connection:")
    dbConn = dbConnection(readConfig())

    if dbConn:
        dbConn.close()
        print("Database connection closed.")
    
if __name__ == "__main__":
    main()
