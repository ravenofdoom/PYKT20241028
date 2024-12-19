# Aufgabe 1: Erstellen eines einfachen Dictionaries 'personen'
# Erstelle ein Dictionary, das die Namen von drei Personen als Schlüssel 
# und ihre Alter als Werte enthält.

print("\nAufgabe 1\n")

personen = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}
print(personen)


# Aufgabe 2: Zugriff auf einen Wert
# Greife auf das Alter einer Person aus dem Dictionary personen zu.

print("\nAufgabe 2\n")

alter_bob = personen["Bob"]
print(alter_bob)


# Aufgabe 3: Hinzufügen eines neuen Eintrags
# Füge einen neuen Eintrag für "David" mit dem Alter 28 zum Dictionary personen hinzu.

print("\nAufgabe 3\n")

personen["David"] = 28
print(personen)


# Aufgabe 4: Ändern eines Wertes
# Ändere das Alter einer Person auf 31 im Dictionary personen.

print("\nAufgabe 4\n")

personen["Alice"] = 31
print(personen)


# Aufgabe 5: Entfernen eines Eintrags
# Entferne eine Person aus dem Dictionary personen.

print("\nAufgabe 5\n")

del personen["Charlie"]
print(personen)


# Aufgabe 6: Überprüfen, ob ein Schlüssel existiert
# Überprüfe, ob der Schlüssel "Eva" im Dictionary personen existiert.

print("\nAufgabe 6\n")

exists = "Eva" in personen
print(exists)


# Aufgabe 7: Iterieren über ein Dictionary
# Iteriere über das Dictionary personen und gebe jeden Schlüssel-Wert-Paar aus.

print("\nAufgabe 7\n")

for name, age in personen.items():
    print(f"{name}: {age}")


# Aufgabe 8: Verschachtelte Dictionaries
# Erstelle ein Dictionary 'personen_info', das Informationen über zwei Personen enthält, wobei jede 
# Person ein eigenes Dictionary mit den Schlüsseln "Name", "Alter" und "Stadt" hat.

print("\nAufgabe 8\n")

personen_info = {
    "Person1": {
        "Name": "Alice",
        "Alter": 30,
        "Stadt": "Berlin"
    },
    "Person2": {
        "Name": "Bob",
        "Alter": 25,
        "Stadt": "Hamburg"
    }
}
print(personen_info)


# Aufgabe 9: Zugriff auf verschachtelte Werte
# Greife auf die Stadt von "Person2" aus dem Dictionary 'personen_info' zu.

print("\nAufgabe 9\n")

stadt_person2 = personen_info["Person2"]["Stadt"]
print(stadt_person2)


# Aufgabe 10: Zusammenführen von Dictionaries
# Erstelle zwei Dictionaries und führe sie zu einem neuen Dictionary zusammen.

print("\nAufgabe 10\n")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)
