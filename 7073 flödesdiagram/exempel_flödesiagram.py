import random
print("Hej och välkommen till tärningsspelet!")
kassa = 100
vill_spela = "ja"
while vill_spela == "ja":
    tärning_1 = random.randint(1, 6)
    tärning_2 = random.randint(1, 6)
    print(tärning_1, tärning_2)

    if tärning_1 == tärning_2:
        kassa = kassa + tärning_1 + tärning_2
        print("Vinst, kassa =", kassa)
    else:
        kassa = kassa - tärning_1 - tärning_2
        print("Förlust, kassa =", kassa)
    vill_spela = input("Vill du spela igen? (ja/nej)")
