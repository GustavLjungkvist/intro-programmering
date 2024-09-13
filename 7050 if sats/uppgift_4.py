text = input("Skriv ett nummer")
tal = int(text)
if tal >=0 and tal <=9 :
    print("är ensiffrigt tal")
if tal >=10 and tal <=99 :
    print("är tvåsiffgrit tal")
if tal >=100 and tal <=999 :
    print("är tresiffrigt tal")
if tal <0 :
    print("ditt tal är negativt")

