import random

def kasta_tarningar(antal):
    return [random.randint(1, 6) for _ in range(antal)]

def visa_tarningar(tarningar):
    print("Tärningar:", ' '.join(map(str, tarningar)))

def spara_tarningar(tarningar):
    val = input("Ange index att spara (0-baserat, separerat med mellanslag): ")
    return [tarningar[i] for i in map(int, val.split()) if 0 <= i < len(tarningar)]

def berakna_poang(kategori, tarningar):
    if kategori in range(1, 7):
        return sum(t for t in tarningar if t == kategori)
    elif kategori == "ett par":
        return max((i * 2 for i in range(6, 0, -1) if tarningar.count(i) >= 2), default=0)
    elif kategori == "två par":
        par = [i for i in range(6, 0, -1) if tarningar.count(i) >= 2]
        return sum(par[:2]) * 2 if len(par) >= 2 else 0
    elif kategori == "tretal":
        return max((i * 3 for i in range(6, 0, -1) if tarningar.count(i) >= 3), default=0)
    elif kategori == "fyrtal":
        return max((i * 4 for i in range(6, 0, -1) if tarningar.count(i) >= 4), default=0)
    elif kategori == "liten stege" and sorted(tarningar) == [1, 2, 3, 4, 5]:
        return 15
    elif kategori == "stor stege" and sorted(tarningar) == [2, 3, 4, 5, 6]:
        return 20
    elif kategori == "kåk":
        par, tretal = 0, 0
        for i in range(1, 7):
            if tarningar.count(i) == 2: par = i
            if tarningar.count(i) == 3: tretal = i
        return par * 2 + tretal * 3 if par and tretal else 0
    elif kategori == "chans":
        return sum(tarningar)
    elif kategori == "yatzy" and len(set(tarningar)) == 1:
        return 50
    return 0

def spela_yatzy():
    poangtabell = {}
    for runda in range(15):
        print(f"Runda {runda + 1}")
        tarningar = kasta_tarningar(5)
        for kast in range(3):
            visa_tarningar(tarningar)
            if kast < 2:
                tarningar = spara_tarningar(tarningar) + kasta_tarningar(5 - len(spara_tarningar(tarningar)))
        kategori = input("Välj kategori: ").lower()
        poangtabell[kategori] = berakna_poang(kategori, tarningar)
        print(f"Du fick {poangtabell[kategori]} poäng i {kategori}.")
    bonus = 50 if sum(poangtabell.get(str(i), 0) for i in range(1, 7)) >= 63 else 0
    print(f"Bonus: {bonus}\nTotalpoäng: {sum(poangtabell.values()) + bonus}")

if __name__ == "__main__":
    spela_yatzy()
