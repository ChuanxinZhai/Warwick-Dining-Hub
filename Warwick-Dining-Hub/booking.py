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
            CREATE TABLE IF NOT EXISTS booking (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                date DATE NOT NULL,
                time TIME NOT NULL,
                guests INTEGER NOT NULL,
                facility TEXT NOT NULL
            )
        ''')
        conn.commit()

# booking function
def add_booking(name, email, date, time, guests, facility):
    with get_db_connection() as conn:
        cur = conn.cursor()
        cur.execute('INSERT INTO booking (name, email, date, time, guests, facility) VALUES (?, ?, ?, ?, ?, ?)',
                    (name, email, date, time, guests, facility))
        conn.commit()


def set_database_path(path):
    global DATABASE
    DATABASE = path


if __name__ == '__main__':
    init_db()
    add_booking('Jordan Bruno', 'Jordan.Bruno@warwick.ac.uk', '2024-02-10', '14:30:00', 4, 'The Beautiful Duck Restaurant')
    add_booking('Chesson Zhai', 'Chesson.Zhai@warwick.ac.uk', '2024-02-15', '19:00:00', 2, 'StarBucks Cafe')
    add_booking('Liping Zheng', 'Liping.Zheng@warwick.ac.uk', '2024-02-20', '18:45:00', 6, 'Terrace Bar')
