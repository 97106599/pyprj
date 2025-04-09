# Opdracht 3 Tekst opslaan
# Naam student: Marrit Kuperus
# Groep: IT2B

def encrypt_tekst(tekst, verschuiving):
    resultaat = ""

    for char in tekst:
        if char.isalpha():

            basis = ord('A') if char.isupper() else ord('a')

            nieuwe_letter = chr((ord(char) - basis + verschuiving) % 26 + basis)
            resultaat += nieuwe_letter
        else:
            resultaat += char

    return resultaat

invoer = input("Geef de tekst die je wilt encrypten..\n")

versleuteld = encrypt_tekst(invoer, 5)
print("\nVersleutelde tekst:")
print(versleuteld)




