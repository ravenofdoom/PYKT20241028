# 1. Erstelle ein Dictionary mit 5 Namen als Keys und dem Alter als Value. 
# Lass dir das Dictionary ausgeben in der Form: „Ralf ist 50 Jahre alt, Marion ist…

print("Aufgabe 1\n")
personen={"Erna": 75, "Rudi": 50, "Frank": 25, "Marion": 30, "Peter": 40}
for key, value in personen.items():
    print(f"{key} ist {value} Jahre alt.", end=" ")
print()

# 2. Berechne aus dem Dictionary aus 1) das Durchschnittsalter.

durchschnitt=sum(personen.values())/len(personen.values())
print(durchschnitt)

# 3. Füge den Values ein weiteres Attribut ‚männlich/weiblich‘ hinzu. 
# Berechne das Durchschnittsalter pro Geschlecht.
print("\nAufgabe 3\n")
personen1={"Erna": [75, "w"], "Rudi": [50, "m"], "Frank": [25, "m"], "Marion": [30, "w"], "Peter": [40, "m"]}

avrAlterFemale=0
cntPersonenFemale=0
avrAlterMale=0
cntPersonenMale=0
for key, value in personen1.items():
    if value[1]=="w":
        avrAlterFemale+=value[0]
        cntPersonenFemale+=1
    else:
        avrAlterMale+=value[0]
        cntPersonenMale+=1

avrAlterFemale/=cntPersonenFemale
print("Durchschnittsalter der Frauen: ", round(avrAlterFemale, 2))
avrAlterMale/=cntPersonenMale
print("Durchschnittsalter der Männer: ", round(avrAlterMale, 2))
print()

# 3. Alternative

personen1={"Erna": [75, "w"], "Rudi": [50, "m"], "Frank": [25, "m"], "Marion": [30, "w"], "Peter": [40, "m"]}

alterFem=list()


# 4: Schreibe die Values aus 1) nun so um, dass sie selbst Dictionaries sind 
#    mit den Keys Geschlecht, Alter, Größe, Gewicht. Berechne die Durchschnitte pro Geschlecht.
print("\nAufgabe 4\n")
personen2={"Erna": {"Geschlecht":"w", "Alter":75, "Groeße":160, "Gewicht":60}, \
           "Rudi": {"Geschlecht":"m", "Alter":50, "Groeße":180, "Gewicht":95}, \
           "Frank": {"Geschlecht":"m", "Alter":25, "Groeße":170, "Gewicht":70}, \
           "Marion": {"Geschlecht":"w", "Alter":30, "Groeße":165, "Gewicht":70}, \
           "Peter": {"Geschlecht":"m", "Alter":40, "Groeße":190, "Gewicht":85}}
avrAgeFem=0
avrSizeFem=0
avrWeightFem=0
cntFem=0
avrAgeMale=0
avrSizeMale=0
avrWeightMale=0
cntMale=0

for k, v in personen2.items():
    for k1, v1 in v.items():
        if v1=="w":
            avrAgeFem+=v.get("Alter")
            avrSizeFem+=v.get("Groeße")
            avrWeightFem+=v.get("Gewicht")
            cntFem+=1
        else:
            avrAgeMale+=v.get("Alter")
            avrSizeMale+=v.get("Groeße")
            avrWeightMale+=v.get("Gewicht")
            cntMale+=1
print(f"Das Durchschnittsalter der Frauen beträgt {round(avrAgeFem/cntFem, 2)}.\n",
      f"Die Durchschnittsgröße der Frauen beträgt {round(avrSizeFem/cntFem, 2)}.\n",
      f"Das Durchschnittgewicht der Frauen beträgt {round(avrWeightFem/cntFem, 2)}.\n")

print(f"Das Durchschnittsalter der Männer beträgt {round(avrAgeMale/cntMale, 2)}.\n",
      f"Die Durchschnittsgröße der Männer beträgt {round(avrSizeMale/cntMale, 2)}.\n",
      f"Das Durchschnittgewicht der Männer beträgt {round(avrWeightMale/cntMale, 2)}.\n")
print()

# 5: Erstelle ein Konsolen- Menu, mit dem ein Kunde begrüßt wird, der dann aus einem 
#    Sortiment Waren in seinen Warenkorb legen kann. Den Waren soll ein Preis zugeordnet sein. 
#    Am Ende soll dem Kunden der Gesamtpreis ausgegeben werden. 
#    (Wer möchte, kann noch einen Bezahlvorgang programmieren ggf. mit Rückgeld.)
print("Aufgabe 5\n")

sortiment={"1":{"Gurke":0.50}, "2":{"Tomate":0.30}, "3":{"Avocado": 1.00}, "4":{"Blumenkohl":2.00}, "5":{"Salat":1.50}}
cart=[]
price=float()
print("Guten Tag. Bitte wählen Sie aus unserem Angebot.\n")

for k, v in sortiment.items():
    for k1, v1 in v.items():
        print(f"{k}:    {k1}....{v1} Euro")
    
        
print("\nBeenden Sie die Eingabe mit 'x'.")
choice=""

while choice != "x":
    choice=input("Warennummer:\n")
    if choice in sortiment.keys():
        cart.append(choice)

for num in cart:
    articel=sortiment.get(num)
    price+=list(articel.items())[0][1]


print(f"Ihr Warenkorb enthält {cart}. Das kostet {price} Euro.")

"""
# Aufgabe 5 Alternative

# Kunden-Daten
kunden = {
    'Marion': {'Geschlecht': 'weiblich', 'Konfektionsgröße': 48, 'Gewicht': 75},
    'Ralf': {'Geschlecht': 'männlich', 'Konfektionsgröße': 42, 'Gewicht': 95},
    'Tim': {'Geschlecht': 'männlich', 'Konfektionsgröße': 31, 'Gewicht': 65},
    'Sandra': {'Geschlecht': 'weiblich', 'Konfektionsgröße': 38, 'Gewicht': 48},
    'Lukas': {'Geschlecht': 'männlich', 'Konfektionsgröße': 22, 'Gewicht': 78}
}

# Sortiment mit Preisen
sortiment = {
    'T-Shirt': 20.0,
    'Hose': 50.0,
    'Pullover': 35.0,
    'Schuhe': 80.0,
    'Mütze': 15.0
}

# Funktion zur Begrüßung des Kunden und zur Auswahl der Waren
def konsolen_menue(kunden_dict, sortiment):
    # Begrüßung
    name = input("Bitte geben Sie Ihren Namen ein: ")
    if name in kunden_dict:
        print(f"Herzlich willkommen, {name}!")
    else:
        print("Sie sind nicht in unserer Kundendatenbank.")
        return

    # Warenkorb
    warenkorb = []
    gesamtpreis = 0.0

    # Auswahl der Waren
    while True:
        print("\\nVerfügbares Sortiment:")
        for ware, preis in sortiment.items():
            print(f"{ware}: {preis}€")
        auswahl = input("Was möchten Sie in den Warenkorb legen? (Beenden mit 'fertig'): ")
        if auswahl.lower() == 'fertig':
            break
        elif auswahl in sortiment:
            warenkorb.append(auswahl)
            gesamtpreis += sortiment[auswahl]
            print(f"{auswahl} wurde zum Warenkorb hinzugefügt.")
        else:
            print("Diese Ware ist nicht verfügbar.")

    # Ausgabe des Gesamtpreises
    print("\\nIhr Warenkorb:")
    for ware in warenkorb:
        print(f"- {ware}")
    print(f"Der Gesamtpreis beträgt: {gesamtpreis:.2f}€")

# Aufruf des Konsolen-Menüs
konsolen_menue(kunden, sortiment)
"""
"""
# Aufgabe 5 Alternative 2
print("Aufgabe 5\n")

# ********************************************************************************************************************
# Definition der Waren und Variablen
waren_sortiment = {"Uhr": 149.90, "Laptop": 799.00, "USB-Stick": 29.95, "Smartphone": 1099.49}

def anzeige_sortiment():
    print("Unser Waren-Sortiment:")
    print("----------------------")
    for ware, preis in waren_sortiment.items():
        print(f"            {ware}: {preis} EUR")
        print(f"             ---------------------")

warenkorb =[]
gesamtpreis_warenkorb = 0

# ******************************************************************************************************************
# Konsolenmenü mit Auswahl der Ware und Anzahl
print("Herzlich Willkommen in unserem Shopping-Center")

modus_wird_ausgefuehrt = True

while modus_wird_ausgefuehrt:
    modus = input("Bitte wählen Sie:\n    (s) Sortiment anzeigen\n    (a) Artikel in Warenkorb legen\n    (w) Warenkorb anzeigen\n    (x) Shop verlassen\n      Hier ihre Auswahl eingeben: ")
    modus = modus.strip()

    if modus == "x":
        print("Auf Wiedersehen, Danke für Ihren Besuch!")
        modus_wird_ausgefuehrt = False

    elif modus == "s":
        anzeige_sortiment()

    elif modus == "a":

        ware_wird_ausgewaehlt = True

        while ware_wird_ausgewaehlt:
            anzeige_sortiment()
            print()
            auswahl_kunde = input("Welche Ware möchten Sie in Ihren Warenkorb legen? (b = Auswahl beenden): ")
            print()

            if auswahl_kunde == "b":
                print("Danke")
                ware_wird_ausgewaehlt = False
                
            elif auswahl_kunde in waren_sortiment:
                menge_wird_gewählt = True

                while menge_wird_gewählt:
                    menge = int(input(f"Bitte die gewünschte Menge für die Ware: {auswahl_kunde} eingeben: "))

                    if 1 <= menge <= 99:         
                        gesamtpreis_warenkorb += waren_sortiment.get(auswahl_kunde)*menge
                        menge_wird_gewählt = False
                    else:
                        print("Menge muss zwischen 1 und 99 liegen!")

                warenkorb.append(auswahl_kunde)
                
                print(f"\n{auswahl_kunde} wurde dem Warenkorb hinzugefügt\n")
            else:
                print(f"{auswahl_kunde} ist nicht im Waren-Sortiment enthalten\n")
 
    elif modus == "w":
        if not warenkorb:
            print("Ihr Warenkorb ist leer!")
        else:
            print("Sie haben bisher folgende Waren in Ihrem Korb abgelegt: \n")
            for ware in range(len(warenkorb)):
                print(warenkorb[ware])
            print(f"Der zu zahlende Gesamtbetrag ist: {gesamtpreis_warenkorb} Euro")

"""

# Schreibe ein Dictionary, das ein Shoppingcenter simuliert mit 5 Geschäften und je 3 Artikeln. 
# Erstelle nun ein Konsolen- Menu, das alle Artikel mit einer Artikelnummer ausgibt. 
# Der Nutzer soll (mehrere) Artikel auswählen können. Nach Verlassen der Auswahl soll dem Nutzer
# ausgegeben werden, in welchen Geschäften er die jeweiligen Artikel findet. 
# (z.B. „Latschen, Stiefel finden Sie bei Reno. Rosen, Nelken finden Sie bei Blume2000. usw…“
print("Aufgabe 6\n")

mall={"Reno":["Stiefel", "Sandalen", "Pantoffel"] ,
      "Blume2000":["Nelken", "Rosen", "Tulpen"],
      "REWE":["Wurst", "Obst", "Brot"],
      "Kik":["Schale", "Stifte", "Schreibblock"],
      "DM":["Seife", "Schwamm", "Deo"]}

print("Guten Tag. Was suchen Sie? (Artikelnummer eingeben)\n")

artNr=0
choice2=""
searchList=[]
findList=dict.fromkeys(mall)
for k, v in findList.items():
    findList[k]=[]
tmpList=[]

for k, v in mall.items():
    for art in v:
        artNr+=1
        print(f"{artNr}....{art}")

while choice2 != "x":
    choice2=input("Artikelnummer:\n")
    if choice2.isnumeric() and int(choice2) in range(1, artNr+1):
        searchList.append(int(choice2))

artNr=0
for k, v in mall.items():
    for art in v:
        artNr+=1
        if artNr in searchList:
            tmpList.append(art)                                
    findList[k]+=tmpList
    tmpList.clear()

for k, v in findList.items():
    for art in v:
        print(f"{art} finden Sie bei {k}")

"""
# Aufgabe 6 Alternative
# Schreibe ein Dictionary, das ein Shoppingcenter simuliert mit 5 Geschäften und je 3 Artikeln. 
# Erstelle nun ein Konsolen- Menu, das alle Artikel mit einer Artikelnummer ausgibt. 
# Der Nutzer soll (mehrere) Artikel auswählen können. 
# Nach Verlassen der Auswahl soll dem Nutzer ausgegeben werden, 
# in welchen Geschäften er die jeweiligen Artikel findet. 
# (z.B. „Latschen, Stiefel finden Sie bei Reno. Rosen, Nelken finden Sie bei Blume2000. usw…“

shoppingcenter = {
    "Deichfrau": {"d1":"Schuhe", "d2":"Stiefel" ,"d3": "Sandalen"},
    "Oldi": {"a1":"Zahnpasta", "a2":"Schokolade" ,"a3":"Möhren"},
    "Zolinda": {"z1":"Hose","z2":"Bluse", "z3":"T-Shirt"},
    "immerschon": {"i1":"Computer", "i2":"Headset", "i3":"Mixer"},
    "Hirnbach": {"h1":"Bohrmaschine", "h2":"Schrauben", "h3":"Hammer"}
    }

def finde_geschaeft(artikel_nr, center):
    for geschaeft, artikel in center.items():
        if artikel_nr in artikel.values():
            return geschaeft
        
def finde_artikel(artikel_nr, center):
    for geschaeft, artikel in center.items():
        for nr, artikelname in artikel.items():
            if artikel_nr in nr:
                return artikelname
            
liste_auswahl_kunde = set()        


auswahl_wird_ausgeführt = True

while auswahl_wird_ausgeführt:

    for shops in shoppingcenter.values():
        for nr, artikel in shops.items():
            print(f"{nr}: {artikel}")

    auswahl = input("Bitte Artikel-Nr. auswählen (z.B.: d1) oder Auswahl verlassen mit (x): ")
    
    if auswahl == "x":        
        if not len(liste_auswahl_kunde):
            print("Sie haben keine Artikel ausgewählt")
        else:
            for shop, items in shoppingcenter.items():

                liste_shop_artikel = []

                for art_nr in liste_auswahl_kunde: 
                    
                    if art_nr in items:
                        liste_shop_artikel.append(finde_artikel(art_nr,shoppingcenter))

                if not liste_shop_artikel:
                    continue
                else:
                    liste_shop_artikel = str(liste_shop_artikel).strip("[]")       
                    print(f"{liste_shop_artikel} finden Sie bei {shop}")                  

        auswahl_wird_ausgeführt = False
        
    else:
        liste_auswahl_kunde.add(auswahl)

"""