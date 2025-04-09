# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

# Genereer een willekeurig getal tussen 1 en 100
geheim_getal = random.randint(1, 100)
aantal_pogingen = 0

geraden = False

while not geraden:
    gok = int(input("Raad mijn geheime getal\n"))
    aantal_pogingen += 1

    if gok < geheim_getal:
        print("hoger")
    elif gok > geheim_getal:
        print("lager")
    else:
        print(f"Je hebt het getal geraden het is {geheim_getal}!")
        print(f"Je hebt het in {aantal_pogingen} keer gedaan")
        geraden = True

