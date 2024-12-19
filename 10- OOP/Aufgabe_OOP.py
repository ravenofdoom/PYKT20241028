"""
Stelle folgenden Sachverhalt objektorientiert dar:

Ein Mensch zieht in ein Haus ein und möbliert es mit Gegenständen aus einem Einrichtungshaus.

Objekte: Mensch, Haus, Geschäft, Ware
"""

class Mensch():
    def __init__(self, Name):
        self.name = Name
        self.wohnen = Haus
        self.konto = 0
        self.hab_und_gut = []
        
    def arbeiten(self, Stundenlohn, Stunden):
        self.konto += Stundenlohn * Stunden

    def einziehen(self, Haus):
        self.wohnen = Haus

    def einkaufen(self, Laden):
        Laden.verkaufen(self)   # Der verkaufen- Funktion wird das Mensch- Objekt übergeben
                                # damit die beiden Klassen kommunzieren können

class Haus():
    def __init__(self, Adresse, Wohnflaeche):
        self.adress = Adresse
        self.wohnflaeche = Wohnflaeche

class Laden():
    def __init__(self):
        self.sortiment = []     # Man könnte auch noch eine 
        self.warenkorb = []     # Kasse hinzufügen
    def verkaufen(self, Kunde:Mensch):
        bestellen = True    # Bool für den While- Loop ab Zeile 57
        bestellliste = []   # Hilfsvariable
        def checkWarenkorb():   # verschachtelte Funktion
            """
            Soll prüfen, ob der Kunde genug 
            Platz und Geld für die Ware hat.
            """   
            areaWare = 0    # kumulierte Fläche
            preisWare = 0   # kumulierter Preis
            for ware in self.warenkorb:
                areaWare+=ware.flaeche
                preisWare+=ware.einkaufspreis*2
            if Kunde.wohnen.wohnflaeche > areaWare and Kunde.konto >= preisWare:
                Kunde.wohnen.wohnflaeche -= areaWare    # Fläche wird bei Kundenadresse abgezogen
                Kunde.konto -= preisWare                # Preis wird beim Kundenkonto abgezogen
                return True
        if self.sortiment:  # Hat der Laden überhaupt etwas anzubieten?
            auswahl = 0
            print("Was möchten Sie? Eingabe x für Beenden")
            for nummer, ware in enumerate(self.sortiment):  # Sortiment auflisten
                    print(f"{nummer+1} : {ware}")
            while bestellen:    # Loop für den Einkaufsvorgang
                auswahl = input("Geben Sie eine Bestellnummer ein oder 'x' für Beenden\n")
                match auswahl:
                    case 'x':   # beschreibt den Kaufprozess nach Beenden der Auswahl
                        bestellen = False
                        if bestellliste:    # hat der Kunde eine Auswahl getroffen?
                            for item in bestellliste:
                                # Dem Warenkorb wird hinzugefügt
                                # und dem Sortiment gleichzeitig entnommen
                                self.warenkorb.append(self.sortiment.pop(item-1))
                            if checkWarenkorb():    # Besteht der Kunde die Prüfung
                                Kunde.hab_und_gut.append(self.warenkorb)    # wird seinem Hab und Gut
                            else:                                           # die Ware hinzugefügt
                                self.sortiment.append(self.warenkorb)   # andernfalls geht die Ware zurück 
                                self.warenkorb.clear()                  # ins Sortiment und der Warenkorb wird geleert
                        else:break  # Wenn der Kunde keine Auswahl getroffen hatte
                    case _:
                        # Hat der Kunde eine Auswahl getroffen, die eine Zahl ist, welche sich in der Range 
                        # der Sortimentsliste befindet
                        if auswahl.isnumeric() and int(auswahl) <= (len(self.sortiment)+1):
                            bestellliste.append(int(auswahl)-1)
                        else: continue
                                    
        else: print("Ich habe nichts mehr zu verkaufen")    # Der Laden hat keine Ware.

    def auffuellen(self,*ware): # Durch *ware (args) können mehrere Objekte übergeben werden.
        for posten in ware:
            self.sortiment.append(posten)


class Waren():
    def __init__(self, Typ, Einkaufspreis, Flaeche = 0):
        self.typ = Typ
        self.einkaufspreis = Einkaufspreis
        self.flaeche = Flaeche
    def __repr__(self): # einkaufspreis*2 = Grobe Kalkulation für den Verkaufspreis
        return f"{self.typ} für {self.einkaufspreis*2} mit einer Fläche von {self.flaeche}"

# ----------------------------------------------------------------------------------------------
# Programmablauf

Fred = Mensch("Fred")   # Objekt Fred (Mensch) wird erstellt
Fred.arbeiten(20, 8)    # Fred arbeitet, um Geld für Einkäufe zu verdienen
print(Fred.konto)

Haus1 = Haus("12345 Bahnhofstr. 10", 50)    # Haus wird erstellt

Fred.einziehen(Haus1)   # Fred zieht in das Haus

print(Fred.wohnen.adress)

Moebelladen = Laden()   # Möbelladen (Laden) wird erstellt

# Möbelladen füllt sein Sortiment auf
# Natürlich können die Warenobjekte auch vorher erstellt werden
# statt wie hier in place
Moebelladen.auffuellen(stuhl:=Waren("Stuhl", 50, 0.25), tisch:=Waren("Tisch", 80, 1))
Fred.einkaufen(Moebelladen)

print(Fred.wohnen.adress)
print(Fred.hab_und_gut)
print(Fred.konto)
print(Fred.wohnen.wohnflaeche)
