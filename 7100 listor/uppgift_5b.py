import random

val = input("Vill du spela? j/n: ")

while val == 'j':
    tarningar = [random.randint(1, 6) for i in range(5)]
    print("Resultat av tärningarna:", tarningar)
    print("Yatzy!" if all(tarning == tarningar[0] for tarning in tarningar) else "Inte yatzy.")
    
    val = input("Vill du spela igen? j/n: ")

print("Vad roligt att du spelade en stund!")
