svar = input("Skriv ett tal som är mellan 40 och 49")
svar = int(svar)
antal_gissningar=1
while svar != 42:
    if svar < 42:
        print("för litet")
    if svar > 42:
        print("för stort")
    svar = input("Du får en chans till. ")
    svar = int(svar)
    antal_gissningar=antal_gissningar + 1
print("rätt")
print(antal_gissningar)
