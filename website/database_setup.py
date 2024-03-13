import sqlite3

# Create or connect to the database
conn = sqlite3.connect('selfcare.db')
cursor = conn.cursor()

# Create Products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')

# Create Users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

# Create Orders table
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
)
''')

# Insert sample products
products_data = [
    ('Face Mask', 'Rejuvenating face mask', 15.99, 50),
    ('Aromatherapy Set', 'Relaxing essential oils', 29.99, 30),
    # Add more products here
]

# Insert sample users
users_data = [
    ('john_doe', 'john@example.com', 'hashed_password'),
    ('jane_smith', 'jane@example.com', 'hashed_password'),
    # Add more users here
]

# Insert data into tables
conn = sqlite3.connect('selfcare.db')
cursor = conn.cursor()

cursor.executemany(
    'INSERT INTO products (name, description, price, stock) VALUES (?, ?, ?, ?)', products_data)
cursor.executemany(
    'INSERT INTO users (username, email, password) VALUES (?, ?, ?)', users_data)

# Commit changes and close connection
conn.commit()
conn.close()
