# 1. Löse eine verschachelte Liste auf:

print("Aufgabe 1\n")

nested_list = [1, [2, [3, 4], 5], 6]
flat_list = []
stack = [nested_list]

# Tipp: Nutze 'isinstance' und die Listenmethode 'append'

print(flat_list)  # [1, 2, 3, 4, 5, 6]



# 2. Lass eine Liste um eine bestimmte Anzahl von Positionen nach rechts rotieren.

print("Aufgabe 2\n")

lst = [1, 2, 3, 4, 5]
rotated_list = []

print(rotated_list)  # [4, 5, 1, 2, 3]



# 3. Schreibe einen Algorithmus, der eine Liste und eine Liste von booleschen Werten
# annimmt und eine neue Liste zurückgibt, die nur die Elemente der ursprünglichen Liste enthält,
# für die der entsprechende boolesche Wert True ist.

print("Aufgabe 3\n")

zahlen=[1, 2, 3, 4, 5]
tf=[True, False, True, False, True]
# zielliste -> [1, 3, 5]

# Tipp: Nutze die Builtin Funktion 'zip'

zielliste = []

print(zielliste)  # [1, 3, 5]



# 4. Schreibe einen Algorithmus, der zwei Listen annimmt und eine neue Liste zurückgibt, 
# die die Elemente der beiden Listen abwechselnd enthält. Wenn die Listen unterschiedliche 
# Längen haben, sollen die restlichen Elemente der längeren Liste am Ende hinzugefügt werden.

print("Aufgabe 4\n")

lst1 = [1, 2, 3]
lst2 = [4, 5, 6, 7]
gemischt = []



print(gemischt)  # [1, 4, 2, 5, 3, 6, 7]



# 5. Verschmelze zwei sortierte Listen so, dass eine neue sortierte Liste entsteht.

print("Aufgabe 5\n")

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged = []


print(merged)  # [1, 2, 3, 4, 5, 6]



# 6. Schreibe einen Algorithmus, der eine verschachtelte Liste annimmt 
# und die Elemente der verschachtelten Liste sortiert. Die Funktion sollte sowohl 
# die Elemente innerhalb der verschachtelten Listen als auch die verschachtelten Listen selbst sortieren.

print("Aufgabe 6\n")

nested_list2 = [[3, 1, 2], [6, 4, 5], [9, 7, 8]]

print(nested_list2)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



# 7. Schreibe einen Algorithmus, der eine verschachtelte Liste annimmt und 
# die Summe aller Elemente in der verschachtelten Liste berechnet.

print("Aufgabe 7\n")

nested_list3 = [1, [2, [3, 4], 5], 6]
total_sum = 0

# Tipp: 'isinstance'

print(total_sum)  # 21


# 8. Erzeuge eine Liste bis 100, in der statt einer durch 5 teilbaren Zahl eine Liste eingefügt wird, 
# die alle bis dorthin durch 5 teilbaren Zahlen enthält. Also: [0,1,2,3,4,[0,5],6,7,8,9,[0,5,10]...

print("Aufgabe 8\n")




# 9. Sortiere eine Liste so um, dass die erste Hälfte und die zweite Hälfte gegeneinander vertauscht werden.

print("Aufgabe 9\n")




# 10. Führe die Listen [1,2,3,4,5] und [8,7,6,5,4] zusammen und entferne die Duplikate, einmal ohne Beachtung der Reihenfolge, 
# einmal mit Beachtung der Reihenfolge.

print("Aufgabe 10\n")

liste10a=[1,2,3,4,5]
liste10b=[8,7,6,5,4]
liste10=[]
print(liste10, "\n")


