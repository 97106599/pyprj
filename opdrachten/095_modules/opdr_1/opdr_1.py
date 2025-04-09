# Opdracht 1 functies
# Naam student: Marrit Kuperus
# Groep: IT2B

import csv

def lees_csv(bestandsnaam):
    try:
        with open(bestandsnaam, mode='r', newline='', encoding='utf-8') as bestand:
            csv_reader = csv.reader(bestand)
            data = list(csv_reader)
            return data
    except FileNotFoundError:
        print(f"Bestand {bestandsnaam} niet gevonden.")
        return None


from my_modules.csv import lees_csv

bestandsnaam = "gegevens.csv"
data = lees_csv(bestandsnaam)

if data:
    for rij in data:
        print(rij)





