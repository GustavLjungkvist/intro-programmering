lista = [1, 3, 3, 4, 3, 6, 3, 2]

antaltreor= 0
for tal in lista:
    if (tal == 3):
        antaltreor = antaltreor + 1
print("Antal treor: ", antaltreor)

print("count antal 3:", lista.count(3))

for i in range(2, 10):
    print(lista[i])
