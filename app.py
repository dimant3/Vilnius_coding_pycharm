## OBJEKTINIS PROGRAMAVIMAS - AUTOMOBILIS 2023-06-13
class Automobilis:
    def __init__(self, spalva, greitis):    #konstruktorius __init__
        self.spalva = spalva
        self.greitis = greitis
        self.uzvesta = False
    def uzvedam_automobili(self):
        if not self.uzvesta:
            print("Automobilis uzsivede")
            self.uzvesta = True
        else:
            print("Automobilis jau yra uzvestas")
    def didinam_greiti(self, kiekis):   #apsirasem metoda
        self.greitis += kiekis
    def uzgesom(self):
        if self.uzvesta:
            print("Automobilis uzgeso")
            self.uzvesta = False
        else:
            print("Automobilis jau uzgesintas")


automobilis = Automobilis("Juoda", 100)     #sukurem objekta
automobilis.uzvedam_automobili()
automobilis.didinam_greiti(33)
print(automobilis.greitis)
print(automobilis.uzgesom())