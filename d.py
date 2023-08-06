import sqlite3


def create_table():
    conn = sqlite3.connect("merch_store.db")
    cursor = conn.cursor()

    # Create a table for storing user information
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            shipping_address TEXT,
            billing_address TEXT,
            registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_data():
    conn = sqlite3.connect("merch_store.db")
    cursor = conn.cursor()

    # Insert sample user data into the "users" table
    cursor.execute("""
        INSERT INTO users (username, email, password, shipping_address, billing_address)
        VALUES (?, ?, ?, ?, ?)
    """, ("john_doe", "john@example.com", "hashed_password", "123 Main St", "456 Billing St"))

    conn.commit()
    conn.close()


def query_data():
    conn = sqlite3.connect("merch_store.db")
    cursor = conn.cursor()

    # Select all users from the "users" table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    create_table()
    insert_data()
    query_data()
