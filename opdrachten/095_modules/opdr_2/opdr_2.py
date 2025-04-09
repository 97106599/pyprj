# Opdracht 1 modules
# Naam student: Marrit Kuperus
# Groep: IT2B

personen = [
    {"voornaam": "Jan", "achternaam": "Van Der Vliet", "plaats": "Amsterdam"},
    {"voornaam": "Jan Jaap", "achternaam": "Siewers", "plaats": "Rotterdam"},
    {"voornaam": "Piet", "achternaam": "De Vries", "plaats": "Den Haag"},
    {"voornaam": "Griet", "achternaam": "Van Der Pol", "plaats": "Leiden"},
    {"voornaam": "Piet", "achternaam": "Pietersen", "plaats": "Den Haag"}
]


def filter(persoon, filterveld, filter):
    """
    Filter de lijst van personen op basis van een opgegeven veld en de beginletters van de filterwaarde.

    :param persoon: lijst van dictionaries met informatie over personen
    :param filterveld: het veld waarop gefilterd moet worden, bijvoorbeeld "voornaam", "achternaam" of "plaats"
    :param filter: de beginletters waarop je wilt filteren
    :return: lijst met gefilterde personen
    """
    gefilterde_personen = []

    for p in persoon:

        if p[filterveld].lower().startswith(filter.lower()):
            gefilterde_personen.append(f"{p['voornaam']} {p['achternaam']}")

    return gefilterde_personen



personen = [
    {"voornaam": "Jan", "achternaam": "Van Der Vliet", "plaats": "Amsterdam"},
    {"voornaam": "Jan Jaap", "achternaam": "Siewers", "plaats": "Rotterdam"},
    {"voornaam": "Piet", "achternaam": "De Vries", "plaats": "Den Haag"},
    {"voornaam": "Griet", "achternaam": "Van Der Pol", "plaats": "Leiden"},
    {"voornaam": "Piet", "achternaam": "Pietersen", "plaats": "Den Haag"}
]


print("Filter voornaam begint met 'ja':")
resultaten = filter(personen, "voornaam", "ja")
for resultaat in resultaten:
    print(resultaat)

print("\nFilter voornaam begint met 'Pie':")
resultaten = filter(personen, "voornaam", "Pie")
for resultaat in resultaten:
    print(resultaat)

print("\nFilter plaats begint met 'd':")
resultaten = filter(personen, "plaats", "d")
for resultaat in resultaten:
    print(resultaat)


