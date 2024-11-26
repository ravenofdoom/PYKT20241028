# 1.    Quadrat einer Zahl berechnen: Schreibe eine Funktion quadrat(x),
#       die das Quadrat einer Zahl zurückgibt.

print("Aufgabe 1\n")

def quadrat(x):
    if type(x)==int or type(x)==float:
        return x*x
    return False 

# Beispielaufruf
print(quadrat(2))

# 2.    Summe von zwei Zahlen: Schreibe eine Funktion summe(a, b), 
#       die die Summe von zwei Zahlen berechnet.

print("\nAufgabe 2\n")

def summe(a, b):
    if (type(a) in [int,float]) and (type(b) in [int,float]):
        return a+b
    else: return "keine Zahlen übergeben"

# Beispielaufruf
print(10,5)         # 15
print(summe("1",2)) # (type(a) in [int,float])->False, somit:"keine Zahlen übergeben"

# 3.    Länge eines Strings: Schreibe eine Funktion laenge(s), 
#       die die Länge eines Strings zurückgibt.

print("\nAufgabe 3\n")

def laenge(string):
    if type(string) == str:
        return len(string)
    else: "kein String übergeben"
        
# Beispielaufruf
print(laenge("Das ist ein String"))



# 4.    Größere Zahl finden: Schreibe eine Funktion groesser(a, b), 
#       die die größere von zwei Zahlen zurückgibt.

print("\nAufgabe 4\n")

def groesser(a,b):
    return a if a>b else b

# Beispielaufruf    
print(groesser(10,15))

# 5.    Umwandlung in Großbuchstaben: Schreibe eine Funktion grossbuchstaben(s), 
#       die einen String in Großbuchstaben umwandelt.

print("\nAufgabe 5\n")

def grossbuchstaben(string):
    if type(string)==str:
        return string.upper()
    else: return "kein String übergeben"

# Beispielaufruf
print(grossbuchstaben("Das ist ein String."))
print(grossbuchstaben({"Hallo":"Dictionary"})) # Muss abgefangen werden, weil kein String übergeben wurde


# 6.    Prüfen auf gerade Zahl: Schreibe eine Funktion ist_gerade(n), 
#       die überprüft, ob eine Zahl gerade ist.

print("\nAufgabe 6\n")

def ist_gerade(zahl):
    if type(zahl)==int:
        if zahl%2==0:
            return f"{zahl} ist eine gerade Zahl."
        else: return f"{zahl} ist eine ungerade Zahl."
    else: return f"{zahl} ist keine Ganzzahl."	

# Beispielaufruf
print(ist_gerade(4))
print(ist_gerade(5))
print(ist_gerade(5.5)) # Muss abgefangen werden, weil keine Ganzzahl übergeben wurde


# 7.    Umkehrung eines Strings: Schreibe eine Funktion umkehren(s), 
#       die einen String umkehrt.

print("\nAufgabe 7\n")

def umkehren(string:str):
    if type(string)==str:
        return "".join(list(string)[::-1])
    else: return f"{string} ist kein String"

# Beispielaufruf    
print(umkehren("HAllo"))


# 8.    Durchschnitt von drei Zahlen: Schreibe eine Funktion durchschnitt(a, b, c), 
#       die den Durchschnitt von drei Zahlen berechnet.

print("\nAufgabe 8\n")

# Diese Funktion funktioniert nur, wenn auch tatsächlich drei Zahlen übergeben wurden
# Andernfalls wirft sie einen Fehler.

def durchschnitt(a,b,c):    
    return (a+b+c)/3

# Beispielaufruf
print(durchschnitt(5,8,10))

# Will man eine allgemeingültige Durchschnittsfunktion
# muss man sich einer Argumentenliste bedienen (*args).

def durchschnitt_variabel(*args):
    print(*args)
    if all([(type(x) in [int,float]) for x in args]):
        return sum(args)/len(args)
    else: return "Nicht nur numerische Argumente übergeben." 

print(durchschnitt_variabel(5.1,8,10, 20))
