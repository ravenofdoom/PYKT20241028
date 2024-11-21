# ALTERNATIVE mit def:

# def software_check():
#     # Erster Entscheidungspunkt
#     funktioniert_anlage = input("Funktioniert die Anlage? (ja/nein): ").strip().lower()

#     if funktioniert_anlage == "ja":
#         print("Fummel bloß nicht dran rum!")
#     else:
#         hat_herumgespielt = input("Hast du daran herumgespielt? (ja/nein): ").strip().lower()
#         if hat_herumgespielt == "ja":
#             print("Du Rindvieh!")
#             hat_es_jemand_gemerkt = input("Hat es jemand gemerkt? (ja/nein): ").strip().lower()
#             if hat_es_jemand_gemerkt == "ja":
#                 print("Pfeife unauffällig 'La Paloma' und verschwinde!")
#             else:
#                 kann_schuld_verschieben = input("Kannst du jemandem die Schuld zuschieben? (ja/nein): ").strip().lower()
#                 if kann_schuld_verschieben == "ja":
#                     print("Alles klar!")
#                 else:
#                     print("Du armes Schwein!")
#         else:
#             verantwortlich = input("Wird man dich verantwortlich machen? (ja/nein): ").strip().lower()
#             if verantwortlich == "ja":
#                 print("Du armes Schwein!")
#             else:
#                 print("Kümmer' dich nicht drum!")

# software_check()

# Start des Programms
antwort = input("Funktioniert die Anlage? (ja/nein): ").strip().lower()

if antwort == "ja":
    print("Fummel bloß nicht dran rum!")
    print("Pfeife unauffällig 'La Paloma' und verschwinde!")
    print("Alles klar!")
else:
    antwort = input("Hast du daran herumgespielt? (ja/nein): ").strip().lower()
    if antwort == "ja":
        print("Du Rindvieh!")
        antwort = input("Hat es jemand gemerkt? (ja/nein): ").strip().lower()
        if antwort == "nein":
            print("Pfeife unauffällig 'La Paloma' und verschwinde!")
            print("Alles klar!")
        elif antwort == "ja":
            print("Du armes Schwein!")
            antwort = input("Kannst du jemandem die Schuld zuschieben? (ja/nein): ").strip().lower()
            if antwort == "ja":
                print("Alles klar!")
            else:
                print("Du armes Schwein!")
    elif antwort == "nein":
        antwort = input("Wird man dich verantwortlich machen? (ja/nein): ").strip().lower()
        if antwort == "ja":
            print("Du armes Schwein!")
        else:
            print("Kümmer' dich nicht drum!")
            print("Alles klar!")



