# Opdracht 4 Tekst opslaan
# Naam student: Marrit Kuperus
# Groep: IT2B


vragen = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]


feestganger = {}


for i, vraag in enumerate(vragen, start=1):
    antwoord = input(f"{i}. {vraag}\n")

    if "voornaam" in vraag:
        feestganger["voornaam"] = antwoord
    elif "achternaam" in vraag:
        feestganger["achternaam"] = antwoord
    elif "drank" in vraag:
        feestganger["drank"] = antwoord
    elif "eten" in vraag:
        feestganger["eten"] = antwoord

with open("feestgangers.txt", "a", encoding="utf-8") as bestand:
    for sleutel, waarde in feestganger.items():
        bestand.write(f"{sleutel}: {waarde}\n")
    bestand.write("\n")

print("Bedankt voor het invullen!")
print("See you at the party.")


