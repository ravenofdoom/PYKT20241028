# Rohdaten aus z.B. CSV 
zr1=[[3,6,9,12],[6,9,12,15], [9,12,15,18]]
zr2=[[4,8,12,16],[8,12,16,20], [12,16,20,24]]
zr3=[[5,10,15,20],[10,15,20,25],[15,20,25,30]]

import sqlite3

# Verbindung zur Datenbank herstellen (oder erstellen, falls sie nicht existiert)
conn = sqlite3.connect('zr_database.db')
cursor = conn.cursor()

# Erstellen der Tabellen
cursor.execute('''
CREATE TABLE IF NOT EXISTS zr_topic (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    zr TEXT UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS zr_data (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Jahr INTEGER,
    dp1 REAL,
    dp2 REAL,
    dp3 REAL,
    dp4 REAL,
    zr_id INTEGER,
    FOREIGN KEY (zr_id) REFERENCES zr_topic(ID)
)
''')

# Daten importieren
zr_topics = [
    ['Topic1',],
    ['Topic2',],
    ['Topic3',],
]

# Zunächst die Themen in die zr_topic Tabelle einfügen
cursor.executemany('INSERT OR IGNORE INTO zr_topic (zr) VALUES (?)', zr_topics)

# Die IDs der eingefügten Themen abrufen
cursor.execute('SELECT ID FROM zr_topic WHERE zr = ?', ('Topic1',))
topic1_id = cursor.fetchone()[0]
cursor.execute('SELECT ID FROM zr_topic WHERE zr = ?', ('Topic2',))
topic2_id = cursor.fetchone()[0]
cursor.execute('SELECT ID FROM zr_topic WHERE zr = ?', ('Topic3',))
topic3_id = cursor.fetchone()[0]

# Daten in die zr_data Tabelle einfügen
zr_data = [
    (2021, 3,6,9,12, topic1_id),
    (2022, 6,9,12,15, topic1_id),
    (2023, 9,12,15,18, topic1_id),
    (2021, 4,8,12,16, topic2_id),
    (2022, 8,12,16,20, topic2_id),
    (2023, 12,16,20,24, topic2_id),
    (2021, 5,10,15,20, topic3_id),
    (2022, 10,15,20,25, topic3_id),
    (2023, 15,20,25,30, topic3_id),
]

cursor.executemany('INSERT INTO zr_data (Jahr, dp1, dp2, dp3, dp4, zr_id) VALUES (?, ?, ?, ?, ?, ?)', zr_data)

# Änderungen speichern
conn.commit()

# Daten abfragen
cursor.execute('SELECT * FROM zr_data')
rows = cursor.fetchall()
print("Daten in zr_data:")
print(rows)
for row in rows:
    print(row)

# Daten ändern
cursor.execute('UPDATE zr_data SET dp1 = 5.5 WHERE Jahr = 2021')
conn.commit()

# Überprüfen, ob die Änderung erfolgreich war
cursor.execute('SELECT * FROM zr_data WHERE Jahr = ?', (2021,))
updated_row = cursor.fetchone()
print("Aktualisierte Daten für Jahr 2021:")
print(updated_row)

"""
# Daten löschen
cursor.execute('DELETE FROM zr_data WHERE Jahr = ? AND zr_id = ?', (2022, topic2_id))
conn.commit()

# Überprüfen, ob die Löschung erfolgreich war
cursor.execute('SELECT * FROM zr_data WHERE Jahr = ? AND zr_id = ?', (2022, topic2_id))
deleted_row = cursor.fetchone()
print("Gelöschte Daten für Jahr 2022 und Topic2:")
print(deleted_row)  # Sollte None zurückgeben, wenn die Löschung erfolgreich war

"""

# Abfrage für die Daten von Topic1 im Jahr 2021
cursor.execute('SELECT * FROM zr_data WHERE Jahr = ? AND zr_id = ?', (2021, topic1_id))
topic1_2021_row = cursor.fetchone()
print("Daten für Topic1 im Jahr 2021:")
print(topic1_2021_row)

# Verbindung schließen
conn.close()
