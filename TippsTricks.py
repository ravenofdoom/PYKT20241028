# Fibunacci mit Turbo

from functools import lru_cache

@lru_cache  # ohne diesen Decorator langsam
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
for i in range(0,40):
    print(f"{i}: {fib(i)}")



# Counter ganz einfach

from collections import Counter

cars = ["Porsche", "Trabant", "BMW", "BMW", "Porsche", "Seat"]
counter = Counter(cars)
print(counter)

# Gruppieren mit Counter

grouped = list(Counter(cars).elements())
print(grouped)



# Max mit key -> häufigstes Auftreten

zahlen = [10,20,10,30,20,40,10,30,20,30,40]
haeufigste_zahl = max(zahlen, key = zahlen.count)
print(haeufigste_zahl)