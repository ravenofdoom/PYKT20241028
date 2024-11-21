# Funktionen sind wiederverwendbare, aufrufbare Algorithmen
# Man kann sie grob unterscheiden in
# -> Funktionen mit/ ohne Parametern (Argumente)
# -> Funktionen mit/ ohne Rückgabewert (return)

# Aufbau: 
# def funktionsname(Argument1, Argument2, usw...)
#       var=irgendeineVariable-nicht zwingend
#       Algorithmus
#       return var(oder eben nicht)

# ohne Argumente und ohne return
def sayHello():
    print("Hello!")

# mit Argumenten und mit return
def Summe(a, b):
    summe=a+b
    return summe
    print("wird nicht mehr ausgeführt") # alles nach return ist toter Code

# Funktionen können intern dokumentiert werden,
# damit andere Nutzer eine Beschreibung bekommen.
# Diese Beschreibung wird z.B. als Mouseovereffekt angezeigt

def Summe(a:int|float, b:int|float)->int|float:
    """
    sums two integers or floats and returns the sum
    """
    summe=a+b
    return summe

# Halte den Mousecursor über "Summe", um die Beschreibung zu sehen
Summe(10,20)

# Eine Funktion kann auch mehrere Returns haben,
# die je nach Ergebnis zurückgegeben werden

def Summe(a:int|float, b:int|float)->int|float:
    """
    sums two integers or floats and returns the sum
    """
    if type(a)==int|float and type(b)==int|float:
        summe=a+b
        return summe
    else:
        return "Es wurden keine Zahlen übergeben"
    
# oder tatsächlich mehrere Returnwerte:

def zuweisung(a,b):
    return a,b

x, y = zuweisung(5,10)

print(x,y)
    
# Eine Funktion kann auf Variablen verschiedener
# Gültigkeitsbereiche zugreifen. Da es möglich ist,
# Funktionen zu verschachteln, gibt es die Gültigkeits-
# bereiche (Scopes) "global", "nonlocal" und "local"

x=5                         # globale Variable x 

def scope():
    x=10                    # nichtlokal für Unterfunktionen, lokal scope()
    def glob():
        global x
        print(f"Globale Variable {x}")
    def nonloc():
        nonlocal x          # sucht in der übergeordneten Ebene, aber nicht global
        print(f"Nichtlokale Variable {x}")
    def loc():
        x=15                # lokal für loc() 
        print(f"Lokale Variable {x}")
    glob()                  # gibt die globale Variable aus
    nonloc()                # gibt die nichtlokale Variable aus
    loc()                   # gibt die lokale Variable aus
    
scope()

# Man kann "pass" verwenden, um Funktionsdefinitionen zunächst offen zu lassen.

def anyFunction():
    pass

# Wenn Funktionen sehr kurz sind, kann man sie i.d.R. 
# als Lambda- Funktionen schreiben. Lambda- Funktionen
# sind "anonyme" Funktionen ohne Symbol im Arbeitsspeicher,
# wodurch sie sehr effizient sind.

# Beispiele Lambda- Funktionen
greater0 = lambda x: x>0    # prüft, ob die Zahl größer 0 ist
print(greater0(10))
mal2 = lambda y: y*2        # verdoppelt die Zahl
print(mal2(5))
summe = lambda a,b: a+b     # addiert zwei Zahlen
print(summe(10,5))

print((lambda z: z%2==0)(4))    # prüft, ob die Zahl in der letzten Klammer gerade ist
                                # beachte: z wurde an der Stelle definiert, wo sie gebraucht
                                # wurde


# Funktionen können default- Parameter haben,
# die überschrieben werden können

def sagHallo(name, anrede="Frau"):
    print(f"Hallo {anrede} {name}!")

sagHallo("Holle")               # -> Hallo Frau Holle!
sagHallo("Koschnik", "Herr")    # -> Hallo Herr Koschnik!


# Wenn aber ohne default- Argumente die Anzahl der
# Parameter in Definition und Aufruf unterschiedlich sind
# kommt es zu Fehlerausgaben

def zweiArgumente(eins, zwei):
    return "Zwei Argumente übergeben"

# zweiArgumente(5)  # -> Traceback (most recent call last):
                    # File "...\tempCodeRunnerFile.py", line 4, in <module>
                    # zweiArgumente(5)
                    # ~~~~~~~~~~~~~^^^
                    # TypeError: zweiArgumente() missing 1 required positional argument: 'zwei'

# Wichtig: Default- Argumente müssen am Ende der Argumentenliste stehen:

# def dreiArgumente(eins="eins", zwei, drei): # Wirft Fehler, da erstes Argument mit default- Wert
#     pass


# Man kann auch eine unbestimmte Anzahl an Argumenten
# übergeben:
# Args und Kwargs (Argumente und Keyword- Argumente)
# um mehrere Argumente zu übernehmen

def aFunction(var, *args, **kwargs):
    '''
    Es muss nicht *args und **kwargs heißen, 
    wichtig sind die Sternchen.
    *args wird als Tupel interpretiert,
    **kwargs als Dictionary.
    '''
    print(f"Das ist die Variable: {var}.")
    print(f"Das ist das Args- Tupel: {args}")
    print(f"Das ist das Kwargs- Dictionary: {kwargs}")
    for value in kwargs.values():
        print(args[0]*value)

aFunction("Var", 5,"m",3.14, kwargs1 = "Hallo", kwargs2 = "Welt")

"""
Ausgabe:
Das ist die Variable: Var.
Das ist das Args- Tupel: (5, 'm', 3.14)
Das ist das Kwargs- Dictionary: {'kwargs1': 'Hallo', 'kwargs2': 'Welt'}
HalloHalloHalloHalloHallo
WeltWeltWeltWeltWelt
"""

# Beispiel Summenfunktion:
# Diese kann ja nicht sinnvoll mit einer konkreten
# Anzahl von Argumenten definiert werden, da es 
# unendlich viele Zahlen gibt.

# Statt also 
def summiere(a,b):
    return a+b

def summiere(*summanden):
    summe=0
    for wert in summanden:
        summe+=wert
    return summe

print(summiere(10,20,30,40))


# Vier interssante Builtin- Funktionen
# all(), any(), filter() und map()

daten = [0,1,0,5,0,60,74,32,5,6,-4,3,6,8,52,-12,1000]

# all
print("Alle Daten zwischen 0 und 100?")
print(all([(lambda x: x>0 and x<100)(x) for x in daten]))
"""
Ausgabe:
Alle Daten zwischen 0 und 100?
False
"""

# any
print("Gibt es Daten gleich 1000 oder drüber?")
print(any([(lambda x: x>=1000)(x) for x in daten]))
"""
Ausgabe:
Gibt es Daten gleich 1000 oder drüber?
True
"""

# filter
# filtert die Daten aus einer Datenreihe gemäß einer Funktion
daten1 = list(filter(lambda x: x>0 and x<100, daten))   
# übrig bleiben die Daten zwischen 0 und 100.
print(daten1)
"""
Ausgabe:
[1, 5, 60, 74, 32, 5, 6, 3, 6, 8, 52]
"""

daten2 = list(filter(lambda x: x<0 or x>=1000, daten))
# übrig bleiben die Daten kleiner 0 und größergleich 1000
print(daten2)
"""
Ausgabe:
[-4, -12, 1000]
"""

# map
# map wendet eine Funktion auf eine Datenreihe an
daten3 = list(map(lambda x: x>0 and x<100, daten))
# True, wenn 'daten' zwischen 0 und 100, sonst False
print(daten3)
"""
Ausgabe:
[False, True, False, True, False, True, True, True, True, True, False, True, True, True, True, False, False]
"""

daten4 = list(map(lambda x: x*2, daten))
# verdoppelt die Daten aus 'daten'
print(daten4)
"""
Ausgabe:
[0, 2, 0, 10, 0, 120, 148, 64, 10, 12, -8, 6, 12, 16, 104, -24, 2000]
"""
