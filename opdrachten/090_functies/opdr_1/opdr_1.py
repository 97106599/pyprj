# Opdracht 1 functies
# Naam student: Marrit Kuperus
# Groep: IT2B

def write_to_file(bestandsnaam, tekst, voeg_nieuwe_regel_toe=True):
    with open(bestandsnaam, "a", encoding="utf-8") as bestand:
        if voeg_nieuwe_regel_toe:
            bestand.write(tekst + "\n")
        else:
            bestand.write(tekst)

            my_tekst = "Schrijf dit maar even in een bestandje"
            my_file = "test.txt"
            write_to_file(my_file, my_tekst)


