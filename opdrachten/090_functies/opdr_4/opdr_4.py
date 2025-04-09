# Opdracht 1 functies
# Naam student: Marrit Kuperus
# Groep: IT2B

def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:

        if persoon["tussenvoegsel"]:
            print(f"{persoon['voornaam']} {persoon['tussenvoegsel']} {persoon['achternaam']}")
        else:
            print(f"{persoon['voornaam']} {persoon['achternaam']}")


namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
