# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:13:40 2018

@author: Fran
"""

import pyodbc
cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HVRHOGF;'
                      'Database=thesis;'
                      'Trusted_Connection=yes;')

cursor = cnxn.cursor()
cursor.execute("select count(*) FROM [thesis].[db_transactions].[NewCombinedTransactions] where fraud_score is not null")

for row in cursor:
    print(row)

                        