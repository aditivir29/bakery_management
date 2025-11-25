📌 Project Overview

The Bakery Management System is a Python-MySQL–based software solution that automates key bakery operations such as product handling, inventory tracking, and staff management.
It replaces manual record-keeping with accurate and efficient CRUD-based database operations.

This project demonstrates concepts of database design, Python–MySQL connectivity, ER modeling, normalization, and real-time data management.

🎯 Key Functionalities
1. Product Management

Add new bakery products

View all product records

Update product price or quantity

Delete existing products

2. Staff Management

Add new staff members

View staff list

Update staff position or salary

Delete staff records

3. Inventory Tracking

Real-time stock updates

Prevention of over-stocking / under-stocking

Accurate, updated quantity records

4. Reporting

Quick reports on products and staff

Helps in planning and decision-making

🛠️ Technologies Used

Programming Language: Python 3.x

Database: MySQL 8.x

Library Used: mysql-connector-python

Interface: Command-Line (CLI)

IDE: VS Code / PyCharm / Any Python Editor

📡 Python–MySQL Connectivity

The project uses mysql.connector to establish connectivity:

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="your_password"
)

mycursor = mydb.cursor()

✔️ Steps in Database Setup:

Install connector

pip install mysql-connector-python


Create database (automatically handled by code)

Create tables for products and staff

Execute CRUD operations

Commit changes to the database

🗄️ Database Design
Database Name: pybakery
1. Products Table
Column	Type	Description
id	INT (PK, AI)	Product ID
name	VARCHAR(50)	Product name
category	VARCHAR(30)	Type (Cake/Bread/Pastry etc.)
price	FLOAT	Product price
quantity	INT	Available units
SQL:
CREATE TABLE IF NOT EXISTS products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(30) NOT NULL,
    price FLOAT NOT NULL,
    quantity INT NOT NULL
);

2. Staff Table
Column	Type	Description
id	INT (PK, AI)	Staff ID
name	VARCHAR(50)	Staff name
gender	CHAR(1)	M/F
position	VARCHAR(30)	Role (Chef/Cashier etc.)
salary	FLOAT	Salary
SQL:
CREATE TABLE IF NOT EXISTS staff(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    gender CHAR(1),
    position VARCHAR(30) NOT NULL,
    salary FLOAT NOT NULL
);

📘 ER Diagram & Normalization
Entities

Product

Staff

Relationship

Logical association (no foreign keys needed)

Normalization Applied

1NF: Atomic fields

2NF: Full dependency on primary keys

3NF: No transitive dependency

Tables follow Third Normal Form (3NF) to ensure efficiency and no redundancy.

🖥️ User Interface (CLI)

The system uses a simple, menu-driven CLI with the following options:

1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. Add Staff
6. View Staff
7. Update Staff
8. Delete Staff
9. Exit


Each option triggers the appropriate SQL operation through Python.

🧪 Testing

Various test cases were executed to validate:

Insert, update, delete operations

Handling invalid input

Database connectivity

Data consistency

All core functionalities passed successfully.

✅ Project Achievements

Successful integration of Python + MySQL

Fully functional CRUD application

Real-time data updates

Error handling for invalid inputs

Scalable design for future enhancements

⚠️ Limitations

No Graphical User Interface (GUI)

No billing or customer module

Reporting is basic (text-based)

🚀 Future Enhancements

GUI using Tkinter / PyQt

Dashboard with charts & analytics

Login system with roles (Admin/Staff)

Billing and invoicing system

Online order management

📂 Project Structure
📦 Bakery-Management-System
│
├── bakery_management.py
└── README.md

📝 Conclusion

The Bakery Management System successfully automates bakery operations by integrating Python with MySQL.
It improves accuracy, reduces manual effort, and provides a scalable foundation for advanced bakery automation systems.
