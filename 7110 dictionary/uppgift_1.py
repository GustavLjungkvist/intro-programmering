def ordlista_program():
    ordlista = {}

    while True:
        val = input("\n1. Lägg till ord\n2. Avsluta\n3. Visa ordlista\n4. Översätt ord\nVälj (1-4): ")

        if val == "1":
            ordlista[input("Ord: ").strip()] = input("Översättning: ").strip()
        elif val == "2":
            print("Avslutar.")
            break
        elif val == "3":
            print(ordlista if ordlista else "Ordlistan är tom.")
        elif val == "4":
            print(ordlista.get(input("Ord: ").strip(), "Finns ej i ordlistan."))
        else:
            print("Ogiltigt val.")

if __name__ == "__main__":
    ordlista_program()

