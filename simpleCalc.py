import colorama
from colorama import Fore, Style
colorama.init()

class Calculator:
    def __init__(self):
        self.result = 100

    def sudetis(self, skaicius):
        self.result += skaicius

    def atimtis(self,skaicius):
        self.result -= skaicius

    def daugyba(self, skaicius):
        self.result *= skaicius

    def dalyba(self, skaicius):
        if skaicius != 0:
            self.result /= skaicius
        else:
            print("Klaida! Dalyba is 0")

    def isvalyti(self):
        self.result = 0

    def get_result(self):
        return self.result
    # kadangi nera print, reikia GET, kuris grazintu suskaiciuota reiksme. Set metodas nustato reiksme, GET gauna.

Skaiciuoklis = Calculator()
while True:
    print("Pasirinkite norima veiksma_> ")
    print("1. Sudetis")
    print("2. Atimtis")
    print("3. Daugyba")
    print("4. Dalyba")
    print("5. Isvalyti")
    pasirinkimas = input("Iveskite pasirinkimo numeri_> ")

    if pasirinkimas == "1":
        skaicius = int(input("Iveskite skaiciu_> "))
        Skaiciuoklis.sudetis(skaicius)

    elif pasirinkimas == "2":
        skaicius = int(input("Iveskite skaiciu_> "))
        Skaiciuoklis.atimtis(skaicius)

    elif pasirinkimas == "3":
        skaicius = int(input("Iveskite skaiciu_> "))
        Skaiciuoklis.daugyba(skaicius)

    elif pasirinkimas == "4":
        skaicius = float(input("Iveskite skaiciu_> "))
        Skaiciuoklis.dalyba(skaicius)

    elif pasirinkimas == "5":
        Skaiciuoklis.isvalyti()

    else:
        print("Nera tokio pasirinkimo")

    print("result:", Fore.RED + str(Skaiciuoklis.get_result()) + Style.RESET_ALL)
    # kiekviena pasirinkima galima taip nuspalvinti pridejus Fore.GREEN
    print()


