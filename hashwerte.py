aSet = set()       # ein leeres Set wird erstellt
print(type(aSet))

aList = [1,2,5,1.1,1.0,"Hallo", "hallo", "Hallo"]

#aSet.add(aList)    # wirft einen Fehler, da Listen mutable sind und
                    # somit keinen einen eindeutigen Hashwert haben

aTuple = (1,2,5,1.1,1.0,"Hallo", "hallo", "Hallo")

aSet.add(aTuple)   # funktioniert, da Tupele immutable sind
                    # fügt das gesamte Tupel als ein Element dem Set zu

print(aSet)

for elem in aTuple:
    print(hash(elem))   # Python- interne Hashfunktion
    aSet.add(elem)      # Wenn Hashwert noch nicht vorhanden im Set
                        # elem wird dem Set hizugefügt
print(aSet)


# Die folgenden Zeilen benötigen die VLC Player Installationsdatei
# im selben Ordner wie die Python Datei (und eine umbenannten Kopie)

# Natürlich können auch andere Dateien stattdessen geprüft werden

print(hash(open('vlc.exe')))    # VLC Player Installationsdatei
print(hash(open('bla.exe')))    # dasselbe, nur umbenannt

# von der Webseite des VLC Players kopierter Hashwert zur Prüfung
# der Echtheit der Datei
hashwert="4bd03202b6633f9611b3fc8757880a9b2b38c7c0c40ed6bcbefec71c0099d493"


import hashlib  # Hashlibary (wird bei Python- Installation mitgeliefert)

with open('bla.exe', 'rb') as file: # öffnet die *exe im Read Bytes - Modus
    filebytes=file.read()   # Bytes als Variable
    h=hashlib.sha256()      # Hashmethode wie auf Webseite angegeben
    h.update(filebytes)     # Anwendung der Methode auf den Byte- Stream
    print(h.hexdigest())    # Ausgabe des Hashs als Hexadezimal
    print(hashwert, hashwert==h.hexdigest())    # Vergleich