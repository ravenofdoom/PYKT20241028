"""Aufgaben CSV:

1. Lese die CSV Dateien Erwerbstaetige, Lohnentwicklung und Konsumentwicklung ein.
2. Entferne die Lehrzeichen in den Werten und wandle die Werte in Zahlen um.
3. Berechne die Steigerung in der Lohnentwicklung. (1970 = 100%)
4. Berechne die Veränderung des Brutto/ Netto- Verhältnisses in der Lohnentwicklung.
5. Berechne das Verhältnis von Produktion und Dienstleistungen über die Zeitreihen.
6. Berechne die Anteile der in der Landwirtschafts-, Forst-, Fischerei- Beschäftigten.
7. Berechne über die Zeitreihen die Anteile der Konsumposten an den Löhnen.
8. Berechne die Differenz von Löhnen und Konsum über die Zeitreihen.
9. Zu den Aufgaben 3-8 stelle das Ergebnis in einem geigneten Diagramm aus der Matplotlib dar.
"""

import csv

# Eine Funktion zum Einlesen einer beliebigen CSV- Datei
def readCSV(sourcepath):
    data = []
    with open(sourcepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";")

        for line in csv_reader:
            values = []
            for element in line:   
                element = element.replace(",", ".")        
                element = element.replace(" ", "")
                values.append(element)
            data.append(values)
    return data

# Eine (nicht ganz konsequente) Funktion, um Strings zu Fließkommazahlen zu wandeln
def convert_float(sourcelist):
    data_converted = [[float(zahl) for zahl in array] for array in sourcelist]
    return data_converted

# Eine Funktion, um beliebig viele Datenreihen in einem Diagramm darzustellen.
def plot_time_series(years, time_series_data, labels, ylabel):
    import matplotlib.pyplot as plt
    import mplcursors   # pip install mplcursors
    """
    Erstellt ein Liniendiagramm für eine generische Anzahl von Zeitreihen.

    :param time_series_data: Liste von Zeitreihen-Daten (jede Zeitreihe ist eine Liste von Werten)
    :param labels: Liste von Bezeichnungen für die Zeitreihen
    """
    # Überprüfen, ob die Anzahl der Zeitreihen und der Bezeichnungen übereinstimmen
    if len(time_series_data) != len(labels):
        raise ValueError("Die Anzahl der Zeitreihen und der Bezeichnungen muss übereinstimmen.")

    # Erstellen des Diagramms
    plt.figure(figsize=(10, 6))

    # Durchlaufen der Zeitreihen und Plotten
    for i, series in enumerate(time_series_data):
        plt.plot(years, series, label=labels[i])

    # Achsen benennen
    plt.xlabel('Jahr')
    plt.ylabel(ylabel)

    # Jahreszahlen an der x-Achse schräg darstellen
    plt.xticks(years, rotation=90)

    # Rasterlinien hinzufügen
    plt.grid(True)

    # Legende hinzufügen
    plt.legend()

    # Hover-Effekt hinzufügen
    cursor = mplcursors.cursor(hover=True)
    mplcursors.HoverMode.Persistent
    cursor.connect("add", lambda sel: sel.annotation.set_text(f'Jahr: {sel.target[0]}\nAnteil: {sel.target[1]:.2f}'))


    # Diagramm anzeigen
    plt.show()

# Datenreihen einlesen (als Listen)
erwerbdata = readCSV('Wirtschaftszahlen/Erwerbstaetige.csv')
konsumdata = readCSV('Wirtschaftszahlen/Konsumentwicklung.csv')
lohndata = readCSV('Wirtschaftszahlen/Lohnentwicklung.csv')

# Auslagern der Tabellenköpfe in eine eigene Variable
erwerbdata_head = erwerbdata.pop(0)

# Konvertieren der Daten zu Floats
erwerbdata = convert_float(erwerbdata)

# Gilt analog für die kommenden zwei Zeilenpaare!
konsumdata_head = konsumdata.pop(0)
konsumdata = convert_float(konsumdata)
lohndata_head = lohndata.pop(0)
lohndata = convert_float(lohndata)

# Variable für die Zeitreihe der individuellen Löhne
lohnentwicklung = [lohn[2] for lohn in lohndata]

# Variable für Steigerung in Prozent bei 1970 == 100%
lohnsteigerung = [(lohn[2]/lohndata[0][2])-1 for lohn in lohndata]

# plot_time_series([x for x in range(1970, 2024)], [lohnsteigerung], ["Lohnsteigerung"], "Steigerung in 100 Prozent")

# Verhältnis von Netto- und Bruttolöhnen
netto_brutto = [lohn[4]/lohn[2] for lohn in lohndata]

# Verhältnis von Angestellten in der Produktion zu denen in Dienstleistungen
prod_dienst = [Angestellter[3]/Angestellter[5] for Angestellter in erwerbdata]

# Anteil der Land-, Forst- und Fischereiarbeiter an den Gesamtbeschäftigten
landForstFisch_gesamt = [Angestellter[2]/Angestellter[1] for Angestellter in erwerbdata]

# plot_time_series([x for x in range(1970, 2024)], [prod_dienst,landForstFisch_gesamt], ["prod_dienst", "landForstFisch_gesamt"], "Anteil in Prozent")
# Jahr;Insgesamt;NahrungGenuss;Kleidung;WohnWasserStromBrenn;Einrichtung;VerkehrNachrichten;Freizeit;BeherbergGastst;Übrige

# Anteile der Konsumposten am Gesamtkonsum
# war gar nicht gefragt, aber ich habs trotzdem gemacht ;)
nahrungGenuss_gesamt = [konsumposten[2]/konsumposten[1] for konsumposten in konsumdata]
kleidung_gesamt = [konsumposten[3]/konsumposten[1] for konsumposten in konsumdata]
wohnWasserStromBrenn = [konsumposten[4]/konsumposten[1] for konsumposten in konsumdata]
einrichtung_gesamt = [konsumposten[5]/konsumposten[1] for konsumposten in konsumdata]
verkehrNachrichten_gesamt = [konsumposten[6]/konsumposten[1] for konsumposten in konsumdata]
freizeit_gesamt = [konsumposten[7]/konsumposten[1] for konsumposten in konsumdata]
beherbergGastst = [konsumposten[8]/konsumposten[1] for konsumposten in konsumdata]
uebrige = [konsumposten[9]/konsumposten[1] for konsumposten in konsumdata]

# Nahrung/Lohn - Verhältnis
nahrungGenuss_lohn = [*list(zip([konsumposten[2] for konsumposten in konsumdata], [gesamtlohn[1] for gesamtlohn in lohndata]))]
nahrungGenuss_lohn_ratio = [pair[0]/pair[1] for pair in nahrungGenuss_lohn]
# plot_time_series([x for x in range(1970, 2024)], [nahrungGenuss_lohn_ratio], ["Anteil der Ausgaben für Nahrungsmittel am Lohn"], "Anteil am Lohn")

# Kleidung/Lohn - Verhältnis
kleidung_lohn = [*list(zip([konsumposten[3] for konsumposten in konsumdata], [gesamtlohn[1] for gesamtlohn in lohndata]))]
kleidung_lohn_ratio = [pair[0]/pair[1] for pair in kleidung_lohn]

# Wohnung/Lohn - Verhältnis
wohnung_lohn = [*list(zip([konsumposten[4] for konsumposten in konsumdata], [gesamtlohn[1] for gesamtlohn in lohndata]))]
wohnung_lohn_ratio = [pair[0]/pair[1] for pair in wohnung_lohn]

# Einrichtung/Lohn - Verhältnis
einrichtung_lohn = [*list(zip([konsumposten[5] for konsumposten in konsumdata], [gesamtlohn[1] for gesamtlohn in lohndata]))]
einrichtung_lohn_ratio = [pair[0]/pair[1] for pair in einrichtung_lohn]

# VerkehrNachrichten/Lohn - Verhältnis
verkehrNachrichten_lohn = [*list(zip([konsumposten[6] for konsumposten in konsumdata], [gesamtlohn[1] for gesamtlohn in lohndata]))]
verkehrNachrichten_lohn_ratio = [pair[0]/pair[1] for pair in verkehrNachrichten_lohn]

# Freizeit/Lohn - Verhältnis
freizeit_lohn = [*list(zip([konsumposten[7] for konsumposten in konsumdata], [gesamtlohn[1] for gesamtlohn in lohndata]))]
freizeit_lohn_ratio = [pair[0]/pair[1] for pair in freizeit_lohn]

# BeherbergGastst/Lohn - Verhältnis
beherbergGastst_lohn = [*list(zip([konsumposten[8] for konsumposten in konsumdata], [gesamtlohn[1] for gesamtlohn in lohndata]))]
beherbergGastst_lohn_ratio = [pair[0]/pair[1] for pair in beherbergGastst_lohn]

# Übrige/Lohn - Verhältnis
uebrige_lohn = [*list(zip([konsumposten[9] for konsumposten in konsumdata], [gesamtlohn[1] for gesamtlohn in lohndata]))]
uebrige_lohn_ratio = [pair[0]/pair[1] for pair in beherbergGastst_lohn]

# Lohn - Konsum - Differenz
lohn_konsum = [*list(zip([gesamtlohn[1] for gesamtlohn in lohndata], [konsumposten[1] for konsumposten in konsumdata]))]
lohn_konsum_diff = [round((pair[0]-pair[1]), 2) for pair in lohn_konsum]

print()

# Datenbank

import sqlite3

# Verbindung zur Datenbank herstellen (oder erstellen, falls sie nicht existiert)
conn = sqlite3.connect('wirtschaftszahlen.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS erwerbstaetige (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Jahr INTEGER,
    Insgesamt INTEGER,
    LandForstFisch INTEGER,
    ProdAll INTEGER,
    ProdBau INTEGER,
    DienstAll INTEGER,
    HandelVerkehrGast INTEGER,
    InformFinanzVermietUnternehmdienst INTEGER,
    OeffentSonstDienst INTEGER
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS konsumentwicklung(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Jahr INTEGER,
    Insgesamt REAL,
    NahrungGenuss REAL,
    Kleidung REAL,
    WohnWasserStromBrenn REAL,
    Einrichtung REAL,
    VerkehrNachrichten REAL,
    Freizeit REAL,
    BeherbergGastst REAL,
    Uebrige REAL)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS lohnentwicklung(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Jahr INTEGER,
    AN_Entgeld_all REAL,
    AN_Entgeld REAL,
    Bruttolöhne REAL,
    Nettolöhne REAL)''')

cursor.executemany('''INSERT INTO erwerbstaetige(
                    Jahr,
                    Insgesamt,
                    LandForstFisch,
                    ProdAll,
                    ProdBau,
                    DienstAll,
                    HandelVerkehrGast,
                    InformFinanzVermietUnternehmdienst,
                    OeffentSonstDienst
                ) VALUES (?,?,?,?,?,?,?,?,?)''', erwerbdata)

cursor.executemany('''INSERT INTO konsumentwicklung(
                        Jahr,
                        Insgesamt,
                        NahrungGenuss,
                        Kleidung,
                        WohnWasserStromBrenn,
                        Einrichtung,
                        VerkehrNachrichten,
                        Freizeit,
                        BeherbergGastst,
                        Uebrige)
                        VALUES (?,?,?,?,?,?,?,?,?,?)''',konsumdata)

cursor.executemany('INSERT INTO lohnentwicklung (\
                   Jahr, \
                   AN_Entgeld_all,\
                   AN_Entgeld,\
                   Bruttolöhne,\
                   Nettolöhne)\
                    VALUES (?, ?, ?, ?, ?)', lohndata)
conn.commit()

print()