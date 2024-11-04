# db/db_config.py

import os

import psycopg2
from configparser import ConfigParser
from psycopg2 import OperationalError

def read_dbConfig():
    """
    Read the database config from config.ini, located in the parent to /src/
    and return as a dictionary.
    """

    config_path = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'config.ini')

    if not os.path.exists(config_path):
        print("Error: Configuration file not found in parent to /src/ \
        directory.")
        return None
                          
    config = ConfigParser()
    config.read(config_path)

    if 'database' in config:
        db_config = {
            'host': config.get('database', 'host'),
            'port': config.get('database', 'port'),
            'database': config.get('database', 'database'),
            'user': config.get('database', 'user'),
            'password': config.get('database', 'password')
        }
        return db_config
    else:
        print("Error: 'database' section not found in config.ini.")
        return None
    

def dbConnection(db_config):
    try:
        connection = psycopg2.connect(**db_config)
        print("Database connection successfully established.")
        return connection

    except OperationalError as e:
        print(f"Error: Could not connect to the database. Details: {e}")
        return None
    
