# Dekoratoren

"""
Dekoratoren dienen als Wrapper für eine andere Funktion 
oder Klasse.

Hier zwei prominente Beispiele:
"""
# Zeitmessung
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'Funktion {func.__name__!r} brauchte {end - start:.4f} Sekunden')
        return result
    return wrapper

@timer
def test():
    a = 0
    for i in range(1_000_000):
        a = i
    print(a)

test()


# Implementierung von Klassen

from dataclasses import dataclass
@dataclass
class Person:
    name: str
    alter: int
    beruf=""

Fred = Person("Fred", 50)

print("Fred")

Tanja = Person("Tanja", 50)

print(Fred<Tanja)
