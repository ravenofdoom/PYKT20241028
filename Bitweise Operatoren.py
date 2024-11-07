# Bitweise Operatoren

a = 1
b = 2
c = 5

# Das VerUNDen von 2 Bitreihen führt im Ergebnis
# zu einer 1, wenn in beiden Bitreihen an derselben
# Stelle eine 1 steht:

#     2^3,2^2,2^1,2^0
# a = 0001 &
# b = 0010
# ________
#     0000

# aber:

# a = 0001 &
# b = 0101
# ________
#     0001

# Das VerODERn von zwei Bitreihen führt im Ergebnis
# zu einer 1, wenn in mindestens einer der beiden 
# Reihen eine 1 steht:

# a = 0001 |
# b = 0010
# ________
#     0011

# Das VerXORn (exklusives ODER) von zwei Bitreihen führt im 
# Ergebnis zu einer 1, wenn in einer (und wirklich NUR! in einer)
# der beiden Bitreihen eine 1 steht:

# a = 0001 ^
# c = 0011
# ________
#     0010


print(a&b)  # Ausgabe: 0
print(a|b)  # Ausgabe: 3  
print(a^c)  # Ausgabe: 4

# not (~) 
# zumindest in Python folgende Kurzformel:
# (Wert+1)*-1 

print(~2)   # Ausgabe: -3
print(~-2)  # Ausgabe: 1

print(~10)  # Ausgabe: -9
print(~-10) # Ausgabe: 11

# Shift- Operatoren 
# verschieben die Bitreihe nach links oder rechts
# und verdoppeln oder halbieren den Wert
  
print(4<<1) # Ausgabe: 8
print(4<<2) # Ausgabe: 16
# 0000 8421
#      0100
print(4>>1) # Ausgabe: 2
print(4>>2) # Ausgabe: 1

print(9>>1)
# 1001 -> 0100 entspricht 9//2 (Floordivision mit 2)

# Apropos Runden (durch Konvertierung zu Integer):
# Stehen 16 Nachkommastellen auf 9, wird "aufgerundet"

a = 5.9999
print(int(a))   # Ausgabe: 5

b = 5.9999_9999_9999_9999
print(int(b))   # Ausgabe: 6

