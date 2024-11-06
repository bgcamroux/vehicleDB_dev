#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""main.py"""

import os
import sys

from PyQt5.QtWidgets import QApplication
 
from db.connection import read_dbConfig as readConfig
from db.connection import dbConnection
from gui.main_window import MainWindow

def main():
    print("Attempt DB connection:")
    dbConn = dbConnection(readConfig())

    if dbConn:
        dbConn.close()
        print("+ Database connection closed.")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
