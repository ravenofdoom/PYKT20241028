# 1. Schreibe eine Funktion, die deinen Namen und dein Alter als Argumente 
# übernimmt und beides in einem Satz ausgibt.

print("Aufgabe 1\n")

# Beispielaufruf
name("Stefan", 54)

# 2.  Schreibe die Funktion aus 1 so um, dass sie einen formatierten String 
# zurück gibt. Dokumentiere dabei intern alle Argumente und Rückgabewerte, 
# sowie deren Datentyp. 

print("\nAufgabe 2\n")

# Beispielaufruf
print(name2("Stefan", 54))

# 3.  Schreibe eine Funktion "Münzwurf", die einen solchen simuliert. Die Häufigkeit
# soll als Argument übergeben werden.

print("\nAufgabe 3\n")

# Beispielaufruf
flipCoin()

# 4.  Schreibe eine Funktion zur Kreisberechnung, die zwei Argumente übernimmt: einen Zahlenwert
# und einen String, der aussagt, ob dieser Zahlenwert als Radius, Umfang oder Fläche zu verstehen ist.
# Radius soll dabei als Defaultwert eingestellt sein. Die Funktion soll dann die jeweils restlichen 
# Werte ausgeben.

print("\nAufgabe 4\n")

# Beispielaufruf
kreis(10)
kreis(20, "a")

# 5.  Schreibe einen Passwortgenerator, der als Argument die Länge des Passwortes übernimmt
# und dieses zurück gibt.

print("\nAufgabe 5\n")

# Beispielaufruf
print(pwgenSimple(20))

# 6.  Schreiben einen weiteren Passwortgenerator, der als Argumente die Anzahl der Zeichen
# aus dem Bereich der Kleinbuchstaben, der Großbuchstaben, der Zahlen und der Sonderzeichen
# übernimmt und ein entsprechendes Passwort zurück gibt.

print("\nAufgabe 6\n")

# Beispielaufruf
print(pwgenPro(2,3,4,4))

