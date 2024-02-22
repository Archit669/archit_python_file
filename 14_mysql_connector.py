# Write a program to establish MySql connectivity with python to insert/update records in a table.

import mysql.connector

class FeeManagementSystem:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = self.connect_to_database()

    def connect_to_database(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            print("Connected to MySQL database successfully.")
            return conn
        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)
            return None

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS fees
                              (id INT AUTO_INCREMENT PRIMARY KEY,
                               student_name VARCHAR(255),
                               fee_amount DECIMAL(10, 2),
                               paid_amount DECIMAL(10, 2))"""
            )
            print("Table 'fees' created successfully.")
        except mysql.connector.Error as e:
            print("Error creating table:", e)

    def add_fee_record(self, student_name, fee_amount, paid_amount):
        try:
            cursor = self.conn.cursor()
            sql = """INSERT INTO fees (student_name, fee_amount, paid_amount)
                     VALUES (%s, %s, %s)"""
            val = (student_name, fee_amount, paid_amount)
            cursor.execute(sql, val)
            self.conn.commit()
            print("Fee record added successfully.")
        except mysql.connector.Error as e:
            print("Error adding fee record:", e)

    def display_fee_records(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("""SELECT * FROM fees""")
            rows = cursor.fetchall()
            print("\nFee Records:")
            print("{:<10} {:<20} {:<15} {:<15}".format("ID", "Student Name", "Fee Amount", "Paid Amount"))
            print("-" * 60)
            for row in rows:
                record_id, student_name, fee_amount, paid_amount = row
                print("{:<10} {:<20} {:<15} {:<15}".format(record_id, student_name, fee_amount, paid_amount))
        except mysql.connector.Error as e:
            print("Error displaying fee records:", e)

    def update_paid_amount(self, record_id, new_paid_amount):
        try:
            cursor = self.conn.cursor()
            sql = """UPDATE fees SET paid_amount = %s WHERE id = %s"""
            val = (new_paid_amount, record_id)
            cursor.execute(sql, val)
            self.conn.commit()
            print("Paid amount updated successfully.")
        except mysql.connector.Error as e:
            print("Error updating paid amount:", e)

    def delete_fee_record(self, record_id):
        try:
            cursor = self.conn.cursor()
            sql = """DELETE FROM fees WHERE id = %s"""
            val = (record_id,)
            cursor.execute(sql, val)
            self.conn.commit()
            print("Fee record deleted successfully.")
        except mysql.connector.Error as e:
            print("Error deleting fee record:", e)

    def close_connection(self):
        self.conn.close()
        print("Connection to MySQL database closed.")

def main():
    host = "localhost"
    user = "root"
    password = "Archit@123"
    database = "fee_management"

    fee_system = FeeManagementSystem(host, user, password, database)
    fee_system.create_table()

    while True:
        print("\n===== Fee Management System Menu =====")
        print("1. Add Fee Record")
        print("2. Display Fee Records")
        print("3. Update Paid Amount")
        print("4. Delete Fee Record")
        print("5. Exit")
        print("=" * 38)
        choice = input("Enter your choice: ")

        if choice == "1":
            student_name = input("Enter student name: ")
            fee_amount = float(input("Enter fee amount: "))
            paid_amount = float(input("Enter paid amount: "))
            fee_system.add_fee_record(student_name, fee_amount, paid_amount)

        elif choice == "2":
            fee_system.display_fee_records()

        elif choice == "3":
            record_id = int(input("Enter the ID of the record to update: "))
            new_paid_amount = float(input("Enter the new paid amount: "))
            fee_system.update_paid_amount(record_id, new_paid_amount)

        elif choice == "4":
            record_id = int(input("Enter the ID of the record to delete: "))
            fee_system.delete_fee_record(record_id)

        elif choice == "5":
            fee_system.close_connection()
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
