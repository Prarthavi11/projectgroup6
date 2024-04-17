# Flask Project : Group 6
The project is based on using Flask framework to design a website to display the selected Dataset and its related information.

## Project Files:
1) main_website.py : Contains the Flask application code including route definitions.
2) templates/ : Directory containing HTML templates for the website. (index_links.html, about.html, data_table.html)
3) data_table.html : HTML page to display the Dataset.
4) about.html : HTML page to display the information related to the dataset.
5) index_links.html : Main HTML page that displays the links of about.html and data_table.html
6) create_db.py : Contains functions for database creation, table creation, and data insertion.
7) README.md : This file providing an overview of the project and instructions for running it.
8) store_data1.csv : Sample CSV file containing data for database insertion.
9) README.md: This file providing an overview of the project and instructions for running it.
10) requirements.txt: File listing all necessary Python packages required for running the project.

## Setting up:
**1) Git Hub clone repository:**
   git clone https://github.com/Prarthavi11/projectgroup6
   
**2) To install the required packages:**
   pip install -r requirements.txt
   
**3) To run the flask Project:**
   python main_website.py

## Process Steps:
1) Visit **http://localhost:5000/** in your web browser to access the home page.
2) Click on the **"Link To About page"** link to view information about the selected dataset.
3) Click on the **"Link To Data page"** link to view the data set.
