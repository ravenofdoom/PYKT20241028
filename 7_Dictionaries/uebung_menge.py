#Aufgabe 1: Grundoperationen auf Mengen
A = {1,2,3,4}
B = {3,4,5,6}
#Berechne die Mengen C = A∪B, D = A∩B, E = A∖B, F = AΔB und gib diese aus.
# Lösung: Anfang
C = A.union(B)
D = A.intersection(B)
E = A.difference(B)
F = A.symmetric_difference(B)
# oder:
C = A | B
D = A & B
E = A - B
F = A ^ B

print(f"{A}union{B}={C}")
print(f"{A}intersec{B}={D}")
print(f"{A}diff{B}={E}")
print(f"{A}symdiff{B}={F}")
# Lösung: Ende


#Aufgabe 2: Menge ergänzen
B={3,5,7,8}
C={3,4,5,6,7,8}

# a) Benenne die Menge A, damit die Vereinigung 𝐴∪𝐵 die Zielmenge C ergibt.
# Lösung: Anfang
A = {4,6}
# oder: 
A = C-B
print(f"Menge A={A}")
# Lösung: Ende

# b) Überprüfe die Korrektheit deiner erstellten Menge A, also dass C=𝐴∪𝐵 gilt.
# Lösung: Anfang
print(A.union(B) == C)
# oder:
print(A|B == C)
# Lösung: Ende

# c) Berechne die Menge A, damit die Vereinigung 𝐴∪𝐵 die Zielmenge C ergibt.
# Lösung: Anfang
A = C.difference(B)
print(f"Menge A={A}")
# Lösung: Ende


# Aufgabe 3: Symmetrische Hülle berechnen
R={(1,2),(3,4),(5,6),(7,8)}
# Berechne die symmetrische Hülle von R. R besteht aus einer Menge von geordneten Paaren.
# Die symmetrische Hülle fügt für jedes Paar (a,b) auch (b,a) hinzu, falls es noch nicht existiert.
huelle_R = set()
# Lösung: Anfang
for a,b in R:
    huelle_R.add( (a,b) )
    huelle_R.add( (b,a) )

print(huelle_R)
# Lösung: Ende
# Erwartes Ergebnis: huelle_R={(1,2),(3,4),(5,6),(7,8),(2,1),(4,3),(6,5),(8,7)}


# Aufgabe 4: Symmetrische Hülle prüfen

# a) Definiere eine Menge A von geordneten Paaren, die eine symmetrische Hülle bildet.
# Lösung: Anfang
A={(1,2),(3,4),(2,1),(4,3)}
# Lösung: Ende

# b) Definiere eine Menge B von geordneten Paaren, die keine symmetrische Hülle bildet.
# Lösung: Anfang
B={(1,2),(3,4),(2,1),(6,7)}
# Lösung: Ende

# c) Schreibe eine Funktion, welche prüft ob eine übergebene Menge von geordneten Paaren eine symmetrische Hülle bildet.
# Lösung: Anfang
def huelle_pruefen(menge: set[(int,int)]) -> bool:
    for a,b in menge:
        if (b,a) not in menge:
            return False
    return True
# Lösung: Ende

# d) Prüfe die Korrektheit der Funktion anhand der Mengen A und B.
# Lösung: Anfang
print(huelle_pruefen(A))
print(huelle_pruefen(B))
# Lösung: Ende


# Aufgabe 5: Mengendifferenz und Mengenrelation
A = {1,2,3,4}
B = {3,4,5,6}

# a) Bestimme eine Menge D so dass C⊆A wobei C=B\D.
# Lösung: Anfang
D = {5,6}
# Lösung: Ende

# b) Überprüfe, dass C⊆A eingehalten wird.
# Lösung: Anfang
C = B.difference(D)
print(C.issubset(A))
# Lösung: Ende


# Aufgabe 6: Symmetrische Differenz erzeugen
C={2,5,8}
B={1,2,3,4,5}

# a) Gib ein Beispiel für eine Menge A an, so dass die symmetrische Differenz C=AΔB gilt.
# Lösung: Anfang
A = {1,3,4,8}
# Lösung: Ende

# b) Überprüfe die Korrektheit deiner erstellten Menge A. Zeige also das C=AΔB gilt.
# Lösung: Anfang
print(C == A.symmetric_difference(B))
# Lösung: Ende

# c) Herausfordernde Aufgabe: Schreibe ein Programm, das die Eingangsmenge A bestimmt, so dass die symmetrische Differenz C=AΔB entsteht.
# Lösung: Anfang
# Mathematische Herleitung:
# A = (A\B) ∪ (A∩B)
# A\B = C\B (für C=AΔB) 
# A∩B = B\C (für C=AΔB)
A = (C.difference(B)).union(B.difference(C))
print(C == A.symmetric_difference(B))
# Lösung: Ende


# Aufgabe 7: Herausfordernde Aufgabe: Potenzmenge berechnen
# Schreibe eine Funktion, welche die Potenzmenge einer gegebenen Menge berechnet. Eine Potenzmenge (P) enthält alle möglichen Teilmengen der gegebenen Menge.
# Beispiel 1: A = {1,2,3}, P = { {}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3} }
# Beispiel 2: A = {1,2}, P = { {}, {1}, {2}, {1,2} }
# Hinweis: Mengen können nur ineinander verschachtelt werden, wenn sie als frozensets(...) anstatt mittels {...} instanziiert werden.
# z.B. anstatt 'menge = {1,2,{3,4,5},6,7})' schreibe 'menge = frozenset([1,2,frozenset([3,4,5]),6,7])'.
# Lösung: Anfang
def potenzmenge_iterativ(menge: frozenset[int]) -> frozenset[frozenset[int]]:
    potenzmengenliste = [menge]

    for menge in potenzmengenliste:
        for element in menge:
            potenzmengenliste.append(frozenset(menge) - {element})

    return frozenset(potenzmengenliste)

A = frozenset({1,2,3,4})
P = potenzmenge_iterativ(A)
for m in P:
    print(m)
# Lösung: Ende
