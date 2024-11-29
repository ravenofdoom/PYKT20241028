import csv # csv- Modul importieren

erwerbdata=[] # Liste zum Schreiben der Zeilen in der csv Datei

with open('Erwerbstaetige.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    next(csv_reader)      # überspringt die Kopfzeile

    for line in csv_reader:
        erwerbdata.append(line)

erwerbdata_head = erwerbdata.pop(0)     # Kopfzeile wird aus 'erwerbdata' entfernt
                                        # und in einer eigenen Liste gespeichert
# print(erwerbdata_head)

# Wie müssen Datenpunkte nachbehandelt werden, damit man damit rechnen kann?
# print(int(erwerbdata[0][2].replace(" ",""))/int(erwerbdata[0][1].replace(" ","")))

# ds = dataset, dp = datapoint
erwerbdata=[[dp.replace(" ", "") for dp in ds] for ds in erwerbdata]    # 1. Schritt: Leerzeichen entfernen
erwerbdata_int=[[int(dp) for dp in ds] for ds in erwerbdata]            # 2. Schritt: Umwandlung zu Integer

erwerbdata_list=[]
for ds in erwerbdata_int:
    erwerbdata_list.append(dict(zip(erwerbdata_head, ds)))  # fügt Dictionaries der Liste hinzu
                                                            # Durch Reißverschlussverfahren besteht
print(erwerbdata_list)                                      # jedes dict aus Bezeichnung und Wert

# Berechnung des Verhältnisses der in Produktion Beschäftigten zu Gesamt
#print(erwerbdata_dict[0]['ProdAll']/erwerbdata_dict[0]['Insgesamt'])

# print(erwerbdata_int)

# Listcomprehension für die gesamte Zeitreihe: Anteil dieses Bereiches an den gesamtbeschäftigten
anteil_LandForstFisch = [ds[2]/ds[1] for ds in erwerbdata_int]

# print(anteil_LandForstFisch)


# Alternativ Einlesen per DictReader
import csv # csv- Modul importieren

erwerbdata=dict()

with open('Erwerbstaetige.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")

    for line in csv_reader:
            erwerbdata.update( {line['Jahr'] : line} )  # Dictionary Comprehension!
print(erwerbdata)