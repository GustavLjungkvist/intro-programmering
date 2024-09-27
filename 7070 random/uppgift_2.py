import random

val = input("Vill du spela? j/n: ")

while val == 'j':
    tarning_1 = random.randint(1, 6)
    tarning_2 = random.randint(1, 6)
    print(tarning_1, tarning_2)
    
    if tarning_1 == 6 and tarning_2 == 6:
        print("sex-vinst")
    elif tarning_1 == tarning_2:
        print("vinst")
    else:
        print("förlust")
    
    val = input("Vill du spela igen? j/n: ")

print("Vad roligt att du spelade en stund!")
