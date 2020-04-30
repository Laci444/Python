class Vedett:
    allomany = ()

    def __init__(self, file_path):
        self.allomany = [item.split(",") for item in open(file_path, encoding="utf-8")]  # ezek list "comprehension"-ök
        # Itt írja ki egy mátrixba az adatokat. Először vesz egy sort aztán tagolja a vesszőknél egy listává, majd a listákat egy külső listába rakja.
        # Az encoding nagyon fontos, különben nem lesz megfelelően beolvasva

    def sasok(self):
        ezek_a_sasok = [item for item in self.allomany if item[0].find("sas") != -1]  # itt egy listába szedi az elemeket, aminek a 0. indexén (vagyis a nevében) talál "sas" stringet
        print("Sasok nevei, eszmei értékük, nyilvántartásba vételük éve: ")
        for i in ezek_a_sasok:
            print(i[0], i[1], i[2], i[3], sep=" | ", end="")  # a "sep" argumentummal a két érték közötti elválasztás variálható

    def sokba_kerul(self):
        dragak = [item for item in self.allomany if int(item[1]) > 750000]  # listába rakja azokat az elemeket, amiben az 1-es indexen nagyob érték van 750000-nél
        print("Drága állatok nevei, eszmei értékük, nyilvántartásba vételük éve: ")
        for i in dragak:
            print(i[0], i[1], i[2], i[3], sep=" | ", end="")  # az "end" argumentummal a print függvény végre beszúrandó stringet lehet módosítani (alapértelmezetten end="\n" vagyis új sor minden print után)

    def kisebb_nagyobb(self):
        nyilvantartasi_ev = [int(item[2]) for item in self.allomany if int(item[2]) != 0]  # az értékek amelyek nem 0
        print(f"Legelőször nyílvántartásba vett: {self.allomany[nyilvantartasi_ev.index(min(nyilvantartasi_ev))][0]}", f"\tEkkor: {min(nyilvantartasi_ev)}", sep="\n")  # minimum kiválasztás algoritmusa
        # az állomány azon indexében, ami a nyilvántartási_év listában a legkisebb érték lévő lista 0. indexén lévő elem
        print(f"Legutoljára nyílvántartásba vett: {self.allomany[nyilvantartasi_ev.index(max(nyilvantartasi_ev))][0]}", f"\tEkkor: {max(nyilvantartasi_ev)}", sep="\n")  # maximum kiválasztás algoritmusa
        # ugyanaz mint az előző csak legnagyobb

    def eszmei_atlag(self):
        eszmei_ertekek = [int(item[1]) for item in self.allomany if int(item[1]) != 0]
        atlag = sum(eszmei_ertekek) // len(eszmei_ertekek)  # a // olyan osztás aminek a végeredménye csak int (vagyis egész szám) lesz
        return atlag


if __name__ == "__main__":
    database = Vedett("vedett.txt") # példányosításnál megadhatjuk a file !relatív! elérési útját
    print()  # azért vannak üres printek mert azt "end" paraméter "\n" vagyis minden print egy új sort kezd
    database.sasok()
    print()
    database.sokba_kerul()
    print()
    print(f"Eszmei értékek átlaga: {database.eszmei_atlag()}")
    print()
    database.kisebb_nagyobb()
