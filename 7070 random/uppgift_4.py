import random

spela = input("Vill du spela? j/n: ")

while spela == 'j':
    tarning_1 = random.randint(1, 9)
    tarning_2 = random.randint(1, 9)
    tarning_3 = random.randint(1, 9)
    print(tarning_1, tarning_2, tarning_3)

    if tarning_1 == 7 and tarning_2 == 7 and tarning_3 == 7:
        print("dubbelvinst")
    elif tarning_1 == tarning_2 == tarning_3:
        print("Vinst")
    
    else:
        print("förlust")
    spela = input("vill du spela igen? j/n:")

print("Tack för att du spelade, välkommen åter!")

