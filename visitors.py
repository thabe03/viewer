import sqlite3


# Fonction pour initialiser la base de données
def init_db():
    conn = sqlite3.connect('visitor.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS visitors (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      ip_address TEXT UNIQUE
    )''')
    conn.commit()
    conn.close()

# vérifie si l'adresse IP est déjà présente dans la base de données
def insert_ip_addr(ip_addr):
    conn = sqlite3.connect('visitor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM visitors WHERE ip_address=?', [ip_addr])
    row = cursor.fetchone()
    if row is not None:
        # l'adresse IP est déjà présente, ne rien faire
        pass
    else:
        # l'adresse IP n'est pas présente, l'insérer dans la table
        cursor.execute('INSERT INTO visitors (ip_address) VALUES (?)', [ip_addr])
        conn.commit()
    conn.close()

# fonction pour récupérer le nombre de visiteurs à partir de la base de données
def get_visitor_count():
    conn = sqlite3.connect('visitor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM visitors')
    count = cursor.fetchone()[0]
    conn.close()
    return count