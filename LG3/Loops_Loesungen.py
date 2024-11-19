# 1. Summe der ersten n natürlichen Zahlen:
# Schreibe ein Programm, das die Summe der ersten n natürlichen Zahlen berechnet.

n = 10
summe = 0
for i in range(1, n+1):
    summe += i
print(summe)

# 2. Durchschnitt berechnen:
# Schreibe ein Programm, das den Durchschnitt einer Liste von Zahlen berechnet.

zahlen = [1, 2, 3, 4, 5]
summe = 0
for zahl in zahlen:
    summe += zahl
durchschnitt = summe / len(zahlen)
print(durchschnitt)

# 3. Zahlenreihe ausgeben:
# Schreibe ein Programm, das die Zahlen von 1 bis 100 ausgibt.

for i in range(1, 101):
    print(i)

# list100=[x for x in range(1,101)]
# print(list100)

# 4. Gerade Zahlen ausgeben:
# Schreibe ein Programm, das alle geraden Zahlen von 1 bis 50 ausgibt.

for i in range(5, 70):
    if i % 2 == 0:
        print(i)

# 5. Quadratzahlen berechnen:
# Schreibe ein Programm, das die Quadratzahlen der ersten 10 natürlichen Zahlen berechnet und ausgibt.

for i in range(1, 11):
    print(i ** 2)

# 6. Liste invertieren:
# Schreibe ein Programm, das eine Liste von Zahlen invertiert.

liste = [1, 2, 3, 4, 5]
invertierte_liste = liste[::-1]
print(invertierte_liste)
for i in range(len(liste)-1, -1, -1):
    invertierte_liste.append(liste[i])
print(invertierte_liste)

# 7. Wörter zählen:
# Schreibe ein Programm, das die Anzahl der Wörter in einem gegebenen Satz zählt.

print("Dies ist ein   Beispielsatz.".split(sep="e"))

satz = "Dies ist ein Beispielsatz."
wörter = satz.split()
anzahl_wörter = len(wörter)
print(anzahl_wörter)

# 8. Multiplikationstabelle:
# Schreibe ein Programm, das die Multiplikationstabelle für eine gegebene Zahl n ausgibt (z.B. für n=5: 5x1=5, 5x2=10, ..., 5x10=50).

n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# 9. Zahlenreihe mit Schrittweite:
# Schreibe ein Programm, das die Zahlen von 1 bis 100 mit einer Schrittweite von 5 ausgibt.

for i in range(1, 101, 5):
    print(i)

# 10. Nested Loops:
# Schreibe ein Programm, das eine Multiplikationstabelle für die Zahlen von 1 bis 10 ausgibt.

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# 11. String umkehren:
# Schreibe ein Programm, das einen gegebenen String umkehrt.

string = "Hallo"
umgekehrt = ""
for char in string:
    umgekehrt = char + umgekehrt
print(umgekehrt)



# 12. Liste von Quadraten:
# Schreibe ein Programm, das eine Liste von Zahlen nimmt und eine neue Liste mit den Quadraten dieser Zahlen erstellt.

zahlen = [1, 2, 3, 4, 5]
quadrate = []
for zahl in zahlen:
    quadrate.append(zahl ** 2)
print(quadrate)

quadrate = []
liste=[1,2]
quadrate.extend(liste)
print(quadrate)
quadrate.append(liste)
print(quadrate)

# 13. Zahlenreihe mit Bedingung:
# Schreibe ein Programm, das die Zahlen von 1 bis 100 ausgibt, aber jede Zahl durch "Fizz" ersetzt, wenn sie durch 3 teilbar ist, und durch "Buzz" ersetzt, wenn sie durch 5 teilbar ist. Wenn sie durch beide teilbar ist, soll "FizzBuzz" ausgegeben werden.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

i= 1
while i <= 100:
    if (i%5 == 0 and i%3 == 0):
        print("FizzBuzz")
    elif(i%5 == 0):
        print("Buzz")
    elif(i%3 == 0):
        print("Fizz")
    else:
        print(i)
    i = i + 1  
 

# 14. Liste von Wörtern filtern:
# Schreibe ein Programm, das eine Liste von Wörtern nimmt und eine neue Liste mit den Wörtern erstellt, die länger als 5 Zeichen sind.

wörter = ["Hallo", "Welt", "Python", "Programmieren", "Code"]
lange_wörter = []
for wort in wörter:
    if len(wort) > 5:
        lange_wörter.append(wort)
print(lange_wörter)

# 15. Matrix ausgeben:
# Schreibe ein Programm, das eine 3x3-Matrix mit Zahlen von 1 bis 9 ausgibt.

matrix = []
zahl = 1
for i in range(3):
    zeile = []
    for j in range(3):
        zeile.append(zahl)
        zahl += 1
    matrix.append(zeile)
for zeile in matrix:
    print(zeile)
    

# 16. Zahlenreihe mit Bedingung und Schrittweite:
# Schreibe ein Programm, das die Zahlen von 1 bis 100 mit einer Schrittweite von 7 ausgibt, aber jede Zahl durch "Boom" ersetzt, wenn sie durch 7 teilbar ist.

for i in range(1, 101, 7):
    if i % 7 == 0:
        print("Boom")
    else:
        print(i)
