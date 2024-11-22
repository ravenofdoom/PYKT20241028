# 1. Schreibe eine Funktion, die deinen Namen und dein Alter als Argumente 
# übernimmt und beides in einem Satz ausgibt.

print("Aufgabe 1\n")

def name(meinName:str, alter:int):        
    print(f"Mein Name ist {meinName} und ich bin {alter} Jahre alt.")

name("Stefan", 54)

# 2.  Schreibe die Funktion aus 1 so um, dass sie einen formatierten String 
# zurück gibt. Dokumentiere dabei intern alle Argumente und Rückgabewerte, 
# sowie deren Datentyp. 

print("\nAufgabe 2\n")

def name2(meinName:str, alter:int|float)->str:
    '''
    @brief: Gibt einen formatierten Vorstellungstext zurück.\n
    @param1: Hier soll der Name hin.\n
    @param2: Hier soll das Alter hin.\n
    @return: Ein formatierter String.
    '''
    return f"Mein Name ist {meinName} und ich bin {alter} Jahre alt."

print(name2("Stefan", 54))

# 3.  Schreibe eine Funktion "Münzwurf", die einen solchen simuliert. Die Häufigkeit
# soll als Argument übergeben werden.

print("\nAufgabe 3\n")

def flipCoin()->None:
    '''
    @brief: Simuliert einen Münzwurf
    '''
    import random
    coin=["Kopf", "Zahl"]
    print(coin[random.randint(0,1)])    #   random.randint(0,1) nimmt entweder den Wert
                                        #   0 oder 1 an, somit coin[0] oder coin[1]

flipCoin()

# 4.  Schreibe eine Funktion zur Kreisberechnung, die zwei Argumente übernimmt: einen Zahlenwert
# und einen String, der aussagt, ob dieser Zahlenwert als Radius, Umfang oder Fläche zu verstehen ist.
# Radius soll dabei als Defaultwert eingestellt sein. Die Funktion soll dann die jeweils restlichen 
# Werte ausgeben.

print("\nAufgabe 4\n")

def kreis(val:int|float, mod:str="r")->None:    # Argument "mod" ist per default mit "r" für Radius belegt
    '''
    mod bezeichnet, welchen Wert die übergebene 
    Variable darstellt
    Radius="r"      Durchmesser="d"
    Fläche="a"      Umfang="u"
    '''
    from math import pi, sqrt   # Import der Mathebibliothek für PI und Wurzelziehen

    match mod:  # die verschiedenen Berechnungen in Abhängigkeit vom Modus
        case "r":
            d=2*val
            a=pi*val**2
            u=pi*2*val
            print(f"Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "d":
            r=val/2
            a=(pi*val**2)/4
            u=pi*val
            print(f"Radius: {round(r, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "a":
            r=sqrt(val/pi)
            d=2*r
            u=pi*2*r
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Umfang: {round(u, 2)}")
        case "u":
            r=val/(2*pi)
            d=2*r
            a=pi*r**2
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}")

kreis(10)       # Aufruf der Funktion mit nur einem Argument (default=Radius)
kreis(20, "a")  # Aufruf mit zwei Argumenten, erster Wert gilt als Fläche

# 5.  Schreibe einen Passwortgenerator, der als Argument die Länge des Passwortes übernimmt
# und dieses zurück gibt.

print("\nAufgabe 5\n")

#   Einfacher Passwortgenerator unter Verwendung der Module 'random' und 'string'
def pwgenSimple(pwLength:int)->str:
    """
    @param pwLength: Integerzahl für die Anzahl der auszugebenen Zeichen
    @return: Zufällige Zeichenkette
    """
    from string import hexdigits, punctuation
    from random import sample 
    pwPool=hexdigits + punctuation
    # print(pwPool)     # nur einkommentieren, um den Zeichenpool zu sehen
    return "".join(sample(pwPool, pwLength))    # Sampleliste wird in einen leeren String gejoint

print(pwgenSimple(20))

# 6.  Schreiben einen weiteren Passwortgenerator, der als Argumente die Anzahl der Zeichen
# aus dem Bereich der Kleinbuchstaben, der Großbuchstaben, der Zahlen und der Sonderzeichen
# übernimmt und ein entsprechendes Passwort zurück gibt.

print("\nAufgabe 6\n")

def pwgenPro1(lows:int, caps:int, nums:int, specs:int=0)->str:  
    # siehe ab Zeile 125, sinngemäß gleich, nur hier unter Verwendung des String- Moduls
    from random import sample, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    lowLetters=sample(ascii_lowercase, lows)
    capLetters=sample(ascii_uppercase, caps)
    numbers=sample(digits, nums)
    specChar=sample(punctuation, specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    shuffle(pw)
    return "".join(pw)

print(pwgenPro1(2,3,4,4))

def pwgenPro2(lows:int, caps:int, nums:int, specs:int=0)->str:
    from random import sample, shuffle
    lowLetters=sample(range(97, 123), lows) # range(97, 123): Kleinbuchstaben im Ascii-Code
    capLetters=sample(range(65, 91), caps)  # range(65, 91): Großbuchstaben im Ascii-Code
    numbers=sample(range(48, 58), nums)     # range(48, 58): Zahlen im Ascii-Code
    specChar=sample(range(35, 39), specs)   # range(35, 39): Einige Soderzeichen im Ascii-Code
    pw=[]                                   # leere Liste angelegt
    pw.extend(lowLetters+capLetters+numbers+specChar)   # und erweitert um die Einzellisten
    pw=[chr(num) for num in pw] # Umwandlung der numerischen Ascii- Entsprechung in Zeichen
    shuffle(pw)                 # Durchmischen
    return "".join(pw)          # und in einen leeren String joinen

print(pwgenPro2(2,3,4,4))