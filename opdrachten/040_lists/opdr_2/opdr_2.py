# Opdracht 2 lists
# Naam student: Marrit Kuperus
# Groep: IT2B

rivier_info = {
    "rijn": ["nederland", "duitsland", "frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())

# Print de naam van de 1e rivier en het 2e land waar deze doorheen stroomt
print(f"De rivier {rivieren[0].capitalize()} stroomt onder andere door {rivier_info[rivieren[0]][1].capitalize()}")

# Print de naam van de 2e rivier en het 1e land waar deze doorheen stroomt
print(f"De rivier {rivieren[1].capitalize()} stroomt onder andere door {rivier_info[rivieren[1]][0].capitalize()}")

# Print de naam van de 3e rivier en het 3e land waar deze doorheen stroomt
print(f"De rivier {rivieren[2].capitalize()} stroomt onder andere door {rivier_info[rivieren[2]][2].capitalize()}")



