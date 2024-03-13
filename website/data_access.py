import sqlite3


def get_all_products():
    conn = sqlite3.connect('selfcare.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    conn.close()
    return products


def get_product_by_id(product_id):
    conn = sqlite3.connect('selfcare.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()

    conn.close()
    return product

# Define other query functions for users and orders
