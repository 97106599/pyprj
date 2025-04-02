# Opdracht 3 input functie
# Naam student: Marrit Kuperus
# Groep: IT2B

pizza_lijst = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

pizza_lijst.sort()
print(pizza_lijst)

pizza_lijst.append('yo-favorito')
print(pizza_lijst)

pizza_lijst.remove('olivio')
print(pizza_lijst)

print(pizza_lijst[:3])

midden_index = len(pizza_lijst) // 2
print([pizza_lijst[midden_index]])

print(pizza_lijst[-3:])


