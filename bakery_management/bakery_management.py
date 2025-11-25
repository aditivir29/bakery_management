print("BAKERY MANAGEMENT SYSTEM")

import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(host="localhost", user="root", passwd="aditi29")
mycursor = mydb.cursor()

# Create and select database
mycursor.execute("CREATE DATABASE IF NOT EXISTS pybakery")
mycursor.execute("USE pybakery")

# Create tables
mycursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(30) NOT NULL,
    price FLOAT NOT NULL,
    quantity INT NOT NULL
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS staff(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    gender CHAR(1),
    position VARCHAR(30) NOT NULL,
    salary FLOAT NOT NULL
)
""")

mydb.commit()

# Main menu
while True:
    print("\n----- MENU -----")
    print("1 = Add new product ")
    print("2 = View all products ")
    print("3 = Update product ")
    print("4 = Delete product ")
    print("5 = Add new staff ")
    print("6 = View all staff ")
    print("7 = Update staff ")
    print("8 = Delete staff ")
    print("9 = Exit")

    ch = int(input("Enter your choice: "))

    # PRODUCTS

    # CREATE - Add new product
    if ch == 1:
        print("\nEnter Product Details:")
        name = input("Product name: ")
        category = input("Category (Cake/Bread/Pastry/etc): ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        mycursor.execute(
            "INSERT INTO products(name, category, price, quantity) VALUES (%s, %s, %s, %s)",
            (name, category, price, quantity)
        )
        mydb.commit()
        print("Product added successfully.")

    # READ - View all products
    elif ch == 2:
        mycursor.execute("SELECT * FROM products")
        data = mycursor.fetchall()
        if not data:
            print("No products found.")
        else:
            print("\nProduct List:")
            for row in data:
                print(f"ID: {row[0]} | Name: {row[1]} | Category: {row[2]} | Price: {row[3]} | Quantity: {row[4]}")

    # UPDATE - Update product details
    elif ch == 3:
        pid = input("Enter Product ID to update: ")
        print("1 = Update Price")
        print("2 = Update Quantity")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_price = float(input("Enter new price: "))
            mycursor.execute("UPDATE products SET price=%s WHERE id=%s", (new_price, pid))
        elif choice == 2:
            new_qty = int(input("Enter new quantity: "))
            mycursor.execute("UPDATE products SET quantity=%s WHERE id=%s", (new_qty, pid))
        else:
            print("Invalid choice.")
            continue
        mydb.commit()
        print("Product updated successfully.")

    # DELETE - Delete a product
    elif ch == 4:
        pid = input("Enter Product ID to delete: ")
        mycursor.execute("DELETE FROM products WHERE id=%s", (pid,))
        mydb.commit()
        print("Product deleted successfully.")

    # STAFF

    # CREATE - Add new staff
    elif ch == 5:
        print("\nEnter Staff Details:")
        name = input("Name: ")
        gender = input("Gender (M/F): ")
        position = input("Position (Chef/Cashier/etc): ")
        salary = float(input("Salary: "))
        mycursor.execute(
            "INSERT INTO staff(name, gender, position, salary) VALUES (%s, %s, %s, %s)",
            (name, gender, position, salary)
        )
        mydb.commit()
        print("Staff member added successfully.")

    # READ - View all staff
    elif ch == 6:
        mycursor.execute("SELECT * FROM staff")
        data = mycursor.fetchall()
        if not data:
            print("No staff members found.")
        else:
            print("\nStaff List:")
            for row in data:
                print(f"ID: {row[0]} | Name: {row[1]} | Gender: {row[2]} | Position: {row[3]} | Salary: {row[4]}")

    # UPDATE - Update staff details
    elif ch == 7:
        sid = input("Enter Staff ID to update: ")
        print("1 = Update Position")
        print("2 = Update Salary")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_pos = input("Enter new position: ")
            mycursor.execute("UPDATE staff SET position=%s WHERE id=%s", (new_pos, sid))
        elif choice == 2:
            new_sal = float(input("Enter new salary: "))
            mycursor.execute("UPDATE staff SET salary=%s WHERE id=%s", (new_sal, sid))
        else:
            print("Invalid choice.")
            continue
        mydb.commit()
        print("Staff record updated successfully.")

    # DELETE - Delete a staff record
    elif ch == 8:
        sid = input("Enter Staff ID to delete: ")
        mycursor.execute("DELETE FROM staff WHERE id=%s", (sid,))
        mydb.commit()
        print("Staff record deleted successfully.")

    # EXIT
    elif ch == 9:
        print("Exiting Bakery Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
