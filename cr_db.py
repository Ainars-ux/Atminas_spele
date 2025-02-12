import sqlite3

db = sqlite3.connect('dati.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXIST rezultati (
            id INTEGER PRIMARY KEY AUTOINCRENT,
            vards TEXT,
            klikski INTEGER NOT NULL,
            laiks INTEGER NOT NULL,
            datums TEXT NOT NULL,          
            )""")
ieraksti = [
    ('Anonīmais', 100, 100, "2020-01-01"),
    ('Anonīmais', 100, 100, "2020-01-01"),
    ('Anonīmais', 100, 100, "2020-01-01"),
    ('Anonīmais', 100, 100, "2020-01-01"),
    ('Anonīmais', 100, 100, "2020-01-01"),
]
sql.executemany('''
INSERT INTO rezultati (vards, klikski, laiks, datums)
                VALUES (?, ?, ?, ?)
''', ieraksti)
db.commit()
db.close()

print("Datubāze un ieraksti izveidoti!")