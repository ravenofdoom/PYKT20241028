# 1. Schreibe ein Programm, das eine Zahl von der Eingabe liest und ausgibt,
# ob die Zahl positiv, negativ oder null ist.

# Programm, das prüft, ob eine Zahl positiv, negativ oder null ist

zahl = float(input("Bitte geben Sie eine Zahl ein: "))

if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")


# print("Aufgabe 1\n")


# 2. Schreibe ein Programm, das eine Zahl von der Eingabe liest und ausgibt,
# ob die Zahl gerade oder ungerade ist.


# Programm, das prüft, ob eine Zahl gerade oder ungerade ist

zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))

if zahl % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")

# print("Aufgabe 2\n")


# 3. Schreibe ein Programm, das eine Zahl von der Eingabe liest und ausgibt,
# ob die Zahl im Bereich von 1 bis 10 liegt.

# Programm, das prüft, ob eine Zahl im Bereich von 1 bis 10 liegt

zahl = float(input("Bitte geben Sie eine Zahl ein: "))

if 1 <= zahl <= 10:
    print("Die Zahl liegt im Bereich von 1 bis 10.")
else:
    print("Die Zahl liegt nicht im Bereich von 1 bis 10.")


# print("Aufgabe 3\n")


# 4. Schreibe ein Programm, das drei Zahlen von der Eingabe liest
# und die größte der drei Zahlen ausgibt.

# Programm, das die größte von drei Zahlen ausgibt

zahl1 = float(input("Bitte geben Sie die erste Zahl ein: "))
zahl2 = float(input("Bitte geben Sie die zweite Zahl ein: "))
zahl3 = float(input("Bitte geben Sie die dritte Zahl ein: "))

if zahl1 >= zahl2 and zahl1 >= zahl3:
    groesste = zahl1
elif zahl2 >= zahl1 and zahl2 >= zahl3:
    groesste = zahl2
else:
    groesste = zahl3

print(f"Die größte Zahl ist: {groesste:.2f}")


# print("Aufgabe 4\n")


# 5. Schreibe ein Programm, das eine Zahl (1-7) von der Eingabe liest
# und den entsprechenden Wochentag ausgibt
# (1: Montag, 2: Dienstag, ..., 7: Sonntag).

# Programm, das den entsprechenden Wochentag zu einer Zahl (1-7) ausgibt

zahl = int(input("Bitte geben Sie eine Zahl zwischen 1 und 7 ein: "))

if zahl == 1:
    tag = "Montag"
elif zahl == 2:
    tag = "Dienstag"
elif zahl == 3:
    tag = "Mittwoch"
elif zahl == 4:
    tag = "Donnerstag"
elif zahl == 5:
    tag = "Freitag"
elif zahl == 6:
    tag = "Samstag"
elif zahl == 7:
    tag = "Sonntag"
else:
    tag = None  # Ungültige Eingabe

if tag:
    print(f"Der {zahl}. Tag der Woche ist {tag}.")
else:
    print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 7 ein.")

# ALTERNATIVE mit Prüfung der Zahl:

# Erweiterte Version mit Fehlerbehandlung

# try:
#     zahl = int(input("Bitte geben Sie eine Zahl zwischen 1 und 7 ein: "))

#     if zahl == 1:
#         tag = "Montag"
#     elif zahl == 2:
#         tag = "Dienstag"
#     elif zahl == 3:
#         tag = "Mittwoch"
#     elif zahl == 4:
#         tag = "Donnerstag"
#     elif zahl == 5:
#         tag = "Freitag"
#     elif zahl == 6:
#         tag = "Samstag"
#     elif zahl == 7:
#         tag = "Sonntag"
#     else:
#         tag = None

#     if tag:
#         print(f"Der {zahl}. Tag der Woche ist {tag}.")
#     else:
#         print("Ungültige Zahl. Bitte geben Sie eine Zahl zwischen 1 und 7 ein.")
# except ValueError:
#     print("Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.")


# print("Aufgabe 5")


# 6. Schreibe ein Programm, das eine Zahl von der Eingabe liest und ausgibt,
# ob die Zahl durch 2, 3 oder 5 teilbar ist.

# Programm, das prüft, ob eine Zahl durch 2, 3 oder 5 teilbar ist

zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))

teilbar = False  # Variable, um zu prüfen, ob die Zahl teilbar ist

if zahl % 2 == 0:
    print("Die Zahl ist durch 2 teilbar.")
    teilbar = True

if zahl % 3 == 0:
    print("Die Zahl ist durch 3 teilbar.")
    teilbar = True

if zahl % 5 == 0:
    print("Die Zahl ist durch 5 teilbar.")
    teilbar = True

if not teilbar:
    print("Die Zahl ist weder durch 2, 3 noch 5 teilbar.")

# ALTERNATIVE mit Ausgabe aller Teilbarkeiten:

# Programm mit zusammenfassender Ausgabe

# zahl = int(input("Bitte geben Sie eine ganze Zahl ein: "))

# teiler_liste = []

# if zahl % 2 == 0:
#     teiler_liste.append(2)

# if zahl % 3 == 0:
#     teiler_liste.append(3)

# if zahl % 5 == 0:
#     teiler_liste.append(5)

# if teiler_liste:
#     teiler_str = ", ".join(map(str, teiler_liste))
#     print(f"Die Zahl ist durch folgende Zahlen teilbar: {teiler_str}.")
# else:
#     print("Die Zahl ist weder durch 2, 3 noch 5 teilbar.")


# 7. Schreibe ein Programm, das zwei Strings von der Eingabe liest und ausgibt,
# ob die Strings gleich sind, der erste String länger ist oder
# der zweite String länger ist.

# Programm, das zwei Strings vergleicht und ihre Länge prüft

string1 = input("Bitte geben Sie den ersten String ein: ")
string2 = input("Bitte geben Sie den zweiten String ein: ")

if string1 == string2:
    print("Die Strings sind gleich.")
elif len(string1) > len(string2):
    print("Der erste String ist länger als der zweite.")
elif len(string1) < len(string2):
    print("Der zweite String ist länger als der erste.")
else:
    print("Die Strings haben die gleiche Länge, sind aber nicht identisch.")


# print("Aufgabe 7")


# 8. Schreibe ein Programm, das einen String und einen Buchstaben von der
# Eingabe liest und ausgibt, ob der Buchstabe im String enthalten ist,
# nicht enthalten ist oder der String leer ist.

# Programm, das prüft, ob ein Buchstabe in einem String enthalten ist

string = input("Bitte geben Sie einen String ein: ")
buchstabe = input("Bitte geben Sie einen Buchstaben ein: ")

if not string:
    print("Der String ist leer.")
elif len(buchstabe) != 1:
    print("Bitte geben Sie genau einen Buchstaben ein.")
elif buchstabe in string:
    print(f"Der Buchstabe '{buchstabe}' ist im String enthalten.")
else:
    print(f"Der Buchstabe '{buchstabe}' ist im String nicht enthalten.")


# print("Aufgabe 8")


# 9. Schreibe ein Programm, das einen String von der Eingabe liest und ausgibt,
# ob der String nur aus Buchstaben, nur aus Zahlen oder
# aus einer Mischung von beiden besteht.

# Programm, das prüft, ob ein String nur aus Buchstaben, nur aus Zahlen oder aus einer Mischung von beiden besteht

string = input("Bitte geben Sie einen String ein: ")

if not string:
    print("Der String ist leer.")
elif string.isalpha():
    print("Der String besteht nur aus Buchstaben.")
elif string.isdigit():
    print("Der String besteht nur aus Zahlen.")
elif string.isalnum():
    print("Der String besteht aus einer Mischung aus Buchstaben und Zahlen.")
else:
    print("Der String enthält Sonderzeichen.")

# ALTERNATIVE MIT DEZIMALZAHLEN UND SONDERZEICHEN:


# string = input("Bitte geben Sie einen String ein: ")

# if not string:
#     print("Der String ist leer.")
# elif string.isalpha():
#     print("Der String besteht nur aus Buchstaben.")
# elif string.isdigit():
#     print("Der String besteht nur aus Ganzzahlen.")
# elif string.isalnum():
#     print("Der String besteht aus einer Mischung aus Buchstaben und Zahlen.")
# else:
#     # Überprüfung auf das Vorhandensein von Dezimalstellen
#     try:
#         # Versuch, den String als Float zu konvertieren, um Kommazahlen abzufangen
#         float(string)
#         print("Der String enthält eine Kommazahl oder Zahl mit Dezimalstellen.")
#     except ValueError:
#         print("Der String enthält Sonderzeichen.")



# print("Aufgabe 9")


# 10. Schreibe ein Programm, das einen String von der Eingabe liest und ausgibt,
# ob der String mit einem bestimmten Suffix (hinterster Teilstring) endet.

# Programm, das prüft, ob ein String mit einem bestimmten Suffix endet

string = input("Bitte geben Sie einen String ein: ")#.strip()
suffix = input("Bitte geben Sie das Suffix ein, nach dem Sie suchen möchten: ")

# While-Schleife, um leere Eingaben zu vermeiden
# while True:
#     string = input("Bitte geben Sie einen String ein: ").strip()
#     if string:
#         break
#     print("Der eingegebene String ist leer. Bitte erneut eingeben.")


if not string:
    print("Der eingegebene String ist leer.")
elif not suffix:
    print("Das eingegebene Suffix ist leer.")

# Umwandeln der Buchstaben in Kleinbuchstaben
# elif string.lower().endswith(suffix.lower()):
#    print(f"Der String endet mit dem Suffix '{suffix}' (Groß-/Kleinschreibung ignoriert).")

elif string.endswith(suffix):
    print(f"Der String endet mit dem Suffix '{suffix}'.")
else:
    print(f"Der String endet nicht mit dem Suffix '{suffix}'.")

# ALTERNATIVE MIT REGEX:

# import restring = input("bitte teile dich mir mit: ")stringende = input("wie lautet das ende deiner eingabe: ")my_regex= re.compile(re.escape(stringende) + r"$")if my_regex.search(string):    print(f"dein String enthält {stringende} am ende")else :    print(f"dein string enthält {stringende} nicht am ende")   

# print("Aufgabe 10")
