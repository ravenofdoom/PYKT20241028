# Listen können alle Datentypen enthalten, auch gemischt
# in einer einzigen Liste
liste_mischmasch=["wort", 3, 3.0, [1,2], (3,4), {"Zensur": 1}]

# Deshalb können Listen eben auch Listen enthalten,
# die wiederum Listen enthalten
nested_list = [1, [2, [3, 4], 5], 6]
#           #  0  ------1-------, 2
print(nested_list[1])       # -> [2, [3, 4], 5] 
print(nested_list[1][1])    # -> [3, 4]
print(nested_list[1][1][0]) # -> 3


listeA=[1,2,3]
print(id(listeA))
listeA[0]=10            # Speicherstelle für listeA bleibt erhalten
print(id(listeA))
listeA=[5,6,7]          # neue Speicherstelle für listeA
listeB=listeA           # listeB hat dieselbe Speicherstelle wie listeA
listeB[1]=10            # Änderung auch in listeA
print("Liste A:",listeA, id(listeA))
print("Liste B:",listeB, id(listeB))
listeB=listeA.copy()    # listeB erhält eine eigene Speicherstelle

print(listeB)   

listeB[2]=10            # Änderung nicht in listeA
print("Liste A:",listeA, id(listeA))
print("Liste B:",listeB, id(listeB))

# Bei Zahlen ist das Default-Verhalten anders, denn sie sind immutable
a=10
b=a
print(id(a), id(b))
a=11

print(a,b, id(a), id(b))

# LIST COMPREHENSION

# Ausdrücke in eckigen Klammern führen einen Generator aus
# der eine Liste erzeugt

listeVon100=[x for x in range(100)] # erzeugt eine Liste von 0 bis 99
listeC=[*listeB]
#listeC=listeB.copy()
print(listeB, listeC)
print(listeB[0], listeC[0])

varA = -15

# verschachteltes if-else in einem Generator
varB = ("mindestens 10" if varA >= 10 else "höchstens 9" if varA >= 0 else "ist negativ")
print(varB)
print(f"Der Wert der Variable varB ist {varB}.")

# Schreibt listeD als alle geraden Zahlen aus der listeVon100
listeD=[x for x in listeVon100 if x%2==0]

# Schreibt listeD als alle geraden Zahlen
# und alle ungeraden Zahlen multipliziert mit 3 aus der listeVon100
listeD=[x if x%2==0 else x*3 for x in listeVon100]

# Schreibt listeD als alle geraden Zahlen,
# alle restlos durch 5 teilbaren Zahlen multipliziert mit 3
# und alle anderen (ungeraden) Zahlen multipliziert mit 10
# aus der listeVon100
listeD=[x if x%2==0 else x*3 if x%5==0 else x*10 for x in listeVon100]
print(listeVon100,"\n\n",listeD)



# List Comprehension in Zugriffsoperator

#   Folgende Aufgabenstellung:
#   Aus der Liste ["Tick", "Trick", "Track", "Bibi", "Baba", "Bubu", "Ulrike"]
#   a) finde den Index von "Track"
#   b) finde die Indizes aller Elemente, die ein "a" enthalten
#   c) zähle die Anzahl der Elemente, die mit "T" beginnen
#   d) finde den Index aller Elemente, die länger als 4 sind
#   Erhöhter Schwierigkeitsgrad: Nutze dazu LC


namen=["Tick", "Trick", "Track", "Bibi", "Baba", "Bubu", "Ulrike"]

# a)
print(next(idx for idx, elem in enumerate(namen) if elem=="Track"))
print(list(idx for idx, elem in enumerate(namen) if elem=="Track")[0])
# b)
print(list(idx for idx, elem in enumerate(namen) if "a" in elem))

# c)
print(len(list(idx for idx, elem in enumerate(namen) if elem.startswith("T"))))

# d)
print(list(idx for idx, elem in enumerate(namen) if len(elem) > 4))

for name in list(idx for idx, elem in enumerate(namen) if len(elem) > 4):
    print(namen[name])

print((idx for idx, elem in enumerate(namen) if elem=="Track"))