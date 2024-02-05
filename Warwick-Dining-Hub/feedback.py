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
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                restaurant TEXT NOT NULL,
                rating INTEGER NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        conn.commit()

# add feedback function
def add_feedback(name, email, restaurant, rating, message):
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO feedback (name, email, restaurant, rating, message) VALUES (?, ?, ?, ?, ?)',
                    (name, email, restaurant, rating, message))
        conn.commit()


def set_database_path(path):
    global DATABASE
    DATABASE = path

if __name__ == '__main__':
    init_db()
    add_feedback('James', 'James@warwick.ac.uk', 'StarBucks Cafe', 5, 'Great coffee and wonderful service!')
    add_feedback('Mark', 'Mark@warwick.ac.uk', 'The Beautiful Duck Restaurant', 4, 'Delicious food and cozy atmosphere.')
    add_feedback('Duncan', 'Duncan@warwick.ac.uk', 'Terrace Bar', 2, 'Bad taste.')
