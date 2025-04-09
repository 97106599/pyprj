# Opdracht 3 condities
# Naam student: Marrit Kuperus
# Groep: IT2B

normale_toegangsprijs = 12.50
kortings_percentages = {
    "baby": 100,
    "kinderen": 50,
    "volwassenen": 0,
    "ouderen": 30
}
leeftijdsgroepen = {
    "baby": (0, 2),
    "kinderen": (3, 18),
    "volwassenen": (19, 64),
    "ouderen": (65, 150)
}

# Vraag de gebruiker om zijn leeftijd
leeftijd_input = int(input("Geef uw leeftijd in aantal jaar\n"))

# Bepaal de leeftijdsgroep
groep = ""
for key, (min_leeftijd, max_leeftijd) in leeftijdsgroepen.items():
    if min_leeftijd <= leeftijd_input <= max_leeftijd:
        groep = key
        break

# Haal het kortingspercentage op
korting = kortings_percentages[groep]
te_betalen = normale_toegangsprijs * (1 - korting / 100)

# Toon de output
print(f"U behoort tot de groep {groep}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt daarom {te_betalen:.2f}")
