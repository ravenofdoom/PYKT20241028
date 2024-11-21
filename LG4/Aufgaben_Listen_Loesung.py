# 1. Löse eine verschachelte Liste auf:

print("Aufgabe 1\n")

nested_list = [1, [2, [3, 4], 5], 6]
flat_list = []
stack = [nested_list]
#print(stack)

while stack:    # entspricht while len(stack)>0
    current = stack.pop()
    for item in current:
        if isinstance(item, list):
            stack.append(item)
            print(stack)
        else:
            flat_list.append(item)

print(flat_list)  # [1, 6, 2, 5, 3, 4]



# 2. Lass eine Liste um eine bestimmte Anzahl von Positionen nach rechts rotieren.

print("Aufgabe 2\n")

lst = [1, 2, 3, 4, 5]
idx = 8
#idx = idx % len(lst)    # 6 % 5 = 1
print(idx)
print(lst[-idx:])
print(lst[:-idx])
rotated_list = lst[-idx:] + lst[:-idx]

print(rotated_list)  # [4, 5, 1, 2, 3]



# 3. Schreibe einen Algorithmus, der eine Liste und eine Liste von booleschen Werten
# annimmt und eine neue Liste zurückgibt, die nur die Elemente der ursprünglichen Liste enthält,
# für die der entsprechende boolesche Wert True ist.

print("Aufgabe 3\n")

zahlen=[1, 2, 3, 4, 5]
#gezippt_zahlen=[(1, True), 2, 3, 4, 5]
tf=[True, False, True, False, True]
# zielliste -> [1, 3, 5]

zielliste = [x for x, b in zip(zahlen, tf) if b]

print(zielliste)  # [1, 3, 5]




# 4. Schreibe einen Algorithmus, der zwei Listen annimmt und eine neue Liste zurückgibt, 
# die die Elemente der beiden Listen abwechselnd enthält. Wenn die Listen unterschiedliche 
# Längen haben, sollen die restlichen Elemente der längeren Liste am Ende hinzugefügt werden.

print("Aufgabe 4\n")

lst1 = [1, 2, 3]
lst2 = [4, 5, 6, 7]
#print(*list(zip(lst1, lst2)))
gemischt = []
len1, len2 = len(lst1), len(lst2)

for i in range(max(len1, len2)):
    if i < len1:
        gemischt.append(lst1[i])
    if i < len2:
        gemischt.append(lst2[i])

print(gemischt)  # [1, 4, 2, 5, 3, 6, 7]



# 5. Verschmelze zwei sortierte Listen so, dass eine neue sortierte Liste entsteht.

print("Aufgabe 5\n")

lst1 = [1, 3, 5]
lst2 = [2, 4, 6]

print(sorted(lst1+lst2))


# alternativ: Hier wird schon durch den if-else Block sortiert.
lst1 = [1, 3, 5]
lst2 = [2, 4, 6]
merged = []
i, j = 0, 0

while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i += 1
    else:
        merged.append(lst2[j])
        j += 1

merged.extend(lst1[i:])
merged.extend(lst2[j:])

print(merged)  # [1, 2, 3, 4, 5, 6]



# 6. Schreibe einen Algorithmus, der eine verschachtelte Liste annimmt 
# und die Elemente der verschachtelten Liste sortiert. Die Funktion sollte sowohl 
# die Elemente innerhalb der verschachtelten Listen als auch die verschachtelten Listen selbst sortieren.

print("Aufgabe 6\n")

nested_list2 = [[3, 1, 2], [6, 4, 5], [9, 7, 8]]

for sublist in nested_list2:
    sublist.sort()

nested_list2.sort()

print(nested_list2)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



# 7. Schreibe einen Algorithmus, der eine verschachtelte Liste annimmt und 
# die Summe aller Elemente in der verschachtelten Liste berechnet.

print("Aufgabe 7\n")

nested_list3 = [1, [2, [3, 4], 5], 6]
total_sum = 0
stack = [nested_list3]

while stack:
    current = stack.pop()
    for item in current:
        if isinstance(item, list):
            stack.append(item)
        else:
            print(item)
            total_sum += item

print(total_sum)  # 21


# 8. Erzeuge eine Liste bis 100, in der statt einer durch 5 teilbaren Zahl eine Liste eingefügt wird, 
# die alle bis dorthin durch 5 teilbaren Zahlen enthält. Also: [0],1,2,3,4,[0,5],6,7,8,9,[0,5,10]...

print("Aufgabe 8\n")

""" def listOf5(x):
    tmpList=[]
    if x%5==0:
        for x in range(x+1):
            if x%5==0:
                tmpList.append(x)
        return tmpList
    else:
        return x
    
print([listOf5(x) for x in range(101)]) """

liste100=[x for x in range(101)]      # Liste per LC erstellt

tmpList=[]      # Hilfsliste
listeOfFive=[]  # Zielliste

for x in liste100:    
    if x%5==0:
        tmpList.append(liste100[x])   # Hilfsliste wird um 5-teilbare Zahl erweitert
        listeOfFive.append(tmpList.copy())  # Hilfsliste wird in der Zielliste eingefügt. Hier Kopie statt Original, weil Listen mutable!
    else:
        listeOfFive.append(liste100[x])   # wenn nicht 5-teilbar, wird einfach nur die Zahl der Zielliste hinzugefügt.

print(listeOfFive)

# 9. Sortiere eine Liste so um, dass die erste Hälfte und die zweite Hälfte gegeneinander vertauscht werden.

print("Aufgabe 9\n")

liste1=[x+1 for x in range(101)]
liste5=liste1[int(((len(liste1))/2)):int(len(liste1))]+liste1[0:int((len(liste1)/2))] #liste1[((len(liste1))/2):len(liste1)]+
liste5=liste1[int(((len(liste1))/2)):]+liste1[:int((len(liste1)/2))] # sparsame Variante liste[50:]+liste[:50]

print(liste5)

# 10. Führe die Listen [1,2,3,4,5] und [8,7,6,5,4] zusammen und entferne die Duplikate, einmal ohne Beachtung der Reihenfolge, 
# einmal mit Beachtung der Reihenfolge.

print("Aufgabe 10\n")

liste6a=[1,2,3,4,5]
liste6b=[8,7,6,5,4]
liste6=liste6a+liste6b
# liste6=list(set(liste6)) # Variante1: Konvertieren der Liste in ein Set, Reihenfolge wird nicht beibehalten
liste6=list(dict.fromkeys(liste6)) # Variante2: fromkeys- Methode des Dictionary nutzen und danach wieder in  eine Liste wandeln
print(liste6, "\n")



