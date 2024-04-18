import sqlite3
import csv
import pandas as pd
def create_db():
    con = sqlite3.connect('store_db.db')
    curr = con.cursor()

    curr.execute('DROP table if exists store_datafinal')

    create_table = """CREATE TABLE if not exists store_datafinal(
                        Row_ID INT PRIMARY KEY,
                        Order_ID VARCHAR(25),
                        Order_Date Date,
                        Customer_Name VARCHAR(100),
                        Segment text,
                        State text,
                        Postal_Code INT,
                        Sub_Category VARCHAR(50),
                        Product_Name Text,
                        Sales DECIMAL(3,2),
                        Quantity INT,
                        Discount DECIMAL(3,2),
                        Profit  DECIMAL(3,2)
                        );"""

    curr.execute(create_table)

    with open("store_data1.csv") as f:
        data1 = csv.reader(f)

        for row in data1:
            print(row)
            if 'Row_ID' in row[0]:
                continue
            curr.execute("INSERT INTO store_datafinal VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12]))
            print('data inserted.!')

    con.commit()
    con.close()
