lista = ["słowo", 1, 2,15, True, False]
print(lista)
for element in lista:
    print(element)
lista.append("Maciek")
lista.remove(2)
print(len(lista))
print("lista po wszystkich zmianach")

for element in lista:
    print(element)

zbior = {1, 2, "Szymon", True, False, 1}
print(zbior)
zbior.add("Antoś")
zbior.remove(2)
print("Szymon" in zbior)
print(zbior)

krotka = (1, 2, 3, "Maciek", "Szymon", "Antek")