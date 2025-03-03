import mysql.connector

class Customer:
    def __init__(self, username, password):
        self.username = username
        self.password = password  

    def register(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Change this to your MySQL username
            password="aswinraj",      # Change this to your MySQL password
            database="bank_db"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM customers WHERE username = %s", (self.username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username already exists! Try a different one.")
        else:
            cursor.execute("INSERT INTO customers (username, password, balance) VALUES (%s, %s, %s)", 
                           (self.username, self.password, 0))
            conn.commit()
            print("Registration successful!")

        conn.close()

    def login(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aswinraj",  # Update this with your MySQL password
            database="bank_db"
        )
        cursor = conn.cursor()

        # Check if the user exists
        cursor.execute("SELECT username FROM customers WHERE username = %s AND password = %s",
                       (self.username, self.password))
        result = cursor.fetchone()

        if result:
            print(f"Login successful! Welcome, {self.username}")
            cursor.close()
            conn.close()
            return True  # ✅ Login successful
        else:
            print("Invalid username or password. Try again!")
            cursor.close()
            conn.close()
            return False  # ❌ Return False if login fails
        
    def withdraw(self, amount):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aswinraj",
            database="bank_db"
        )
        cursor = conn.cursor()

        # Get the current balance
        cursor.execute("SELECT balance FROM customers WHERE username = %s", (self.username,))
        result = cursor.fetchone()
        current_balance = result[0] if result else 0

        if current_balance >= amount:
            cursor.execute("UPDATE customers SET balance = balance - %s WHERE username = %s", (amount, self.username))
            conn.commit()

            # Fetch and display the updated balance
            cursor.execute("SELECT balance FROM customers WHERE username = %s", (self.username,))
            result = cursor.fetchone()
            new_balance = result[0] if result else 0

            print(f"Withdrawal successful! Your new balance is: {new_balance}")
        else:
            print("Insufficient balance!")

        cursor.close()
        conn.close()


    def deposit(self, amount):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aswinraj",  # Update this with your MySQL password
            database="bank_db"
        )
        cursor = conn.cursor()

        # Update balance for the logged-in user
        cursor.execute("UPDATE customers SET balance = balance + %s WHERE username = %s", (amount, self.username))
        conn.commit()

        # Fetch and display the updated balance
        cursor.execute("SELECT balance FROM customers WHERE username = %s", (self.username,))
        result = cursor.fetchone()
        new_balance = result[0] if result else 0

        print(f"Deposit successful! Your new balance is: {new_balance}")

        cursor.close()
        conn.close()
    def show_balance(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="aswinraj",
            database="bank_db"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT balance FROM customers WHERE username = %s", (self.username,))
        result = cursor.fetchone()
        balance = result[0] if result else 0

        print(f"Your current balance is: {balance}")

        cursor.close()
        conn.close()
    
