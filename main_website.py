from flask import Flask, render_template
import sqlite3
import pathlib
import csv
from create_db import create_db

db_name = "store_db.db"
create_db() # calling function that creates database, creates table and insert data into table

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index_links.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM store_datafinal limit 20")
    furniture = cursor.fetchall()

    conn.close()
    return render_template("data_table.html", furniture=furniture)

if __name__=="__main__":
    app.run(debug=True)