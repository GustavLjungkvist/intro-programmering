import random

tärningskast = [random.randint(1, 6) for i in range(10)]
sorterade_kast = sorted(tärningskast)
total_summa = sum(sorterade_kast)
medelvärde = total_summa / len(sorterade_kast)
minsta_värde = sorterade_kast[0]
största_värde = sorterade_kast[-1]
antal_sexor = sorterade_kast.count(6)

print("Resultat av tärningskast:", tärningskast)
print("Sorterade kast:", sorterade_kast)
print("Total summa:", total_summa)
print("Medelvärde:", medelvärde)
print("Minsta värde:", minsta_värde)
print("Största värde:", största_värde)
print("Antal sexor:", antal_sexor)
print("Klart")