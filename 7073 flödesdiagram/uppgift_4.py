tal = int(input("Skriv ett tal?"))

if tal >=0 and tal <=9 :
    print("är ensiffrigt tal")
elif tal >=10 and tal <=99 :
    print("är tvåsiffgrit tal")
elif tal >=100 and tal <=999 :
    print("är tresiffrigt tal")
elif tal <0 :
    print("ditt tal är negativt")

