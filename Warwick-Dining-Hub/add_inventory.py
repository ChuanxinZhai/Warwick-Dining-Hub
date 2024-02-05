import sqlite3

DATABASE = 'Dining_Hub.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  
    return conn

def init_db():
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                size TEXT NOT NULL,
                image TEXT,
                facility TEXT NOT NULL
            )
        ''')
        conn.commit()

# add product function
def add_product(name, category, price, size, image=None, facility=''):
    with get_db_connection() as conn:
        cur = conn.cursor()
        # Check if the product already exists
        cur.execute('SELECT * FROM product WHERE name = ? AND category = ?', (name, category))
        existing_product = cur.fetchone()
        if existing_product is None:
            # Product does not exist, add new product
            cur.execute('INSERT INTO product (name, category, price, size, image, facility) VALUES (?, ?, ?, ?, ?, ?)',
                        (name, category, price, size, image, facility))
            print(f"Added new product: {name}")
        else:
            # Product already exists, skip
            print(f"Product already exists: {name}")
        conn.commit()

def set_database_path(path):
    global DATABASE
    DATABASE = path

if __name__ == '__main__':
    # Initialize database (required for first run only)
    init_db()
    add_product('Americano', 'Coffee', 2.5,'200ml', 'Americano.png', 'StarBucks Cafe')
    add_product('Latte', 'Coffee', 3.0, '300ml', 'Latte.png', 'StarBucks Cafe')
    add_product('Cappuccino', 'Coffee', 3.0, '200ml', 'Cappuccino.png', 'StarBucks Cafe')
    add_product('Caramel macchiato', 'Coffee', 3.0, '250ml', 'Caramel_macchiato.png', 'StarBucks Cafe')
    add_product('Hamburger', 'Food', 9.0, '600g', 'Hamburger.png', 'The Beautiful Duck Restaurant')
    add_product('Sandwich', 'Food', 7.5, '450g', 'Sandwich.png', 'The Beautiful Duck Restaurant')
    add_product('Chips', 'Food', 1.5, '100g', 'Chips.png', 'The Beautiful Duck Restaurant')
    add_product('Ramen', 'Food', 8.0, '800g', 'Ramen.png', 'The Beautiful Duck Restaurant')
    add_product('Hot dog', 'Food', 2.5, '100g', 'Hot_dog.png', 'The Beautiful Duck Restaurant')
    add_product('Mojito', 'Wine', 6.0, '400ml', 'Mojito.png', 'Terrace Bar')
    add_product('Margarita', 'Wine', 5.0, '200ml', 'Margarita.png', 'Terrace Bar')
    add_product('Tequila sunrise', 'Wine', 5.5, '400ml', 'Tequila_sunrise.png', 'Terrace Bar')
    add_product('Long island iced tea', 'Wine', 7.0, '450ml', 'Long_island_iced_tea.png', 'Terrace Bar')
    add_product('Beer', 'Wine', 3.0, '600ml', 'Beer.png', 'Terrace Bar')
    add_product('Whiskey', 'Wine', 10.0, '500ml', 'Whiskey.png', 'Terrace Bar')
    add_product('Vodka', 'Wine', 11.0, '500ml', 'Vodka.png', 'Terrace Bar')
    add_product('Gin', 'Wine', 11.5, '500ml', 'Gin.png', 'Terrace Bar')
    add_product('Rice', 'Food', 1.0, '300g', 'Rice.png', 'The Beautiful Duck Restaurant')
    add_product('Steak', 'Food', 15.0, '1000g', 'Steak.png', 'The Beautiful Duck Restaurant')
    add_product('Barbecue', 'Food', 20.0, '1200g', 'Barbecue.png', 'The Beautiful Duck Restaurant')
    add_product('Pizza', 'Food', 7.0, '700g', 'Pizza.png', 'The Beautiful Duck Restaurant')
    add_product('Spaghetti', 'Food', 8.0, '900g', 'Spaghetti.png', 'The Beautiful Duck Restaurant')
    add_product('Curry', 'Food', 6.0, '800g', 'Curry.png', 'The Beautiful Duck Restaurant')
    add_product('Espresso', 'Coffee', 2.8, '300ml', 'Espresso.png', 'StarBucks Cafe')
    add_product('Mocha', 'Coffee', 3.3, '400ml', 'Mocha.png', 'StarBucks Cafe')
    add_product('Blackcafe', 'Coffee', 2.3, '350ml', 'Blackcafe.png', 'StarBucks Cafe')
    add_product('Frappuccino', 'Coffee', 5.0, '370ml', 'Frappuccino.png', 'StarBucks Cafe')
    add_product('Italian coffee', 'Coffee', 3.0, '280ml', 'Italian_coffee.png', 'StarBucks Cafe')
    add_product('Milk', 'Coffee', 1.5, '250ml', 'Milk.png', 'StarBucks Cafe')
    add_product('Cider', 'Wine', 3.5, '330ml', 'Cider.png', 'Terrace Bar')
    add_product('Brandy', 'Wine', 10.5, '300ml', 'Brandy.png', 'Terrace Bar')
    add_product('Rum', 'Wine', 12.5, '400ml', 'Rum.png', 'Terrace Bar')
    