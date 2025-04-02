# Opdracht 2 berekeningen
# Naam student: Marrit Kuperus
# Groep: IT2B
# Hier komt je code...

gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print (gasten)

gasten.remove("Marie")
print(gasten)

index_kees = gasten.index("Kees")  # Vind de positie van Kees
gasten.insert(index_kees + 1, "George")  # Voeg George toe na Kees
print(gasten)
