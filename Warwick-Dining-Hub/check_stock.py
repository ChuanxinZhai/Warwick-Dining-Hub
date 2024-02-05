import sqlite3

DATABASE = 'Dining_Hub.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row 
    return conn

# check stock function
def fetch_products():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM product')
    products = cur.fetchall()
    conn.close()
    return products

def set_database_path(path):
    global DATABASE
    DATABASE = path


if __name__ == '__main__':
    products = fetch_products()
    for product in products:
        print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Size: {product['size']}, Image: {product['image']}")
