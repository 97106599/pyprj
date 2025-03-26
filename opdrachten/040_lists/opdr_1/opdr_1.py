# Opdracht 1 lists
# Naam student: Marrit Kuperus
# Groep: IT2B

# Maak een lege lijst
mylist = []

# Maak vier dictionaries met gegevens van personen
dict_1 = {"id": 0, "voornaam": "Emma", "achternaam": "Jansen"}
dict_2 = {"id": 1, "voornaam": "Noah", "achternaam": "Peters"}
dict_3 = {"id": 2, "voornaam": "Liam", "achternaam": "Vermeer"}
dict_4 = {"id": 3, "voornaam": "Sophie", "achternaam": "De Vries"}

# Voeg de dictionaries toe aan de lijst met een list-methode
mylist.extend([dict_1, dict_2, dict_3, dict_4])

# Print de volledige naam van de 2e persoon (index 1)
print(mylist[1]["voornaam"], mylist[1]["achternaam"])


