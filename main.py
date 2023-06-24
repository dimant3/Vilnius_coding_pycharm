# -------- 2023 - 06 - 19 paskaita --------------------
# 1. parasykit programa kuri atspaudina visus lyginius skaicius nuo 1 iki 10.
# for i in range(11):
#     if i % 2 == 0:
#         print(i)
# galima ir: for i in range(2,11,2) pradeda nuo 2 iki 10 imtinai ir pateikia kas antra skaiciu (paskutinis 2)

# 2. Sukurkite sarasa, kuriame yra keletas skaiciu. Naudojant for cikla, apskaiciuokite saraso skaiciu suma.
# list = [5, 15, 35, 100]
# print(sum(list))

# 2. su for ciklu
# list = [5, 15, 35, 100]
# suma = 0
#
# for skaicius in list:
#     suma += skaicius
# print("Saraso skaiciu suma:", suma)


# 3.Parašykite programą, kuri atspausdina visus skaičius nuo 1 iki 20, tačiau jei skaičius yra dalijamas iš 3,
# atspausdinkite "Fizz", jei skaičius yra dalijamas iš 5, atspausdinkite "Buzz";
# for i in range(1,21):
#     if i % 3 == 0 and i % 5 ==0:
#         print(str(i) + " FizzBuzz")
#     elif i % 3 == 0:
#         print(str(i) + " Fizz")
#     elif i % 5 == 0:
#         print(str(i) + " Buzz")

# 4. Sukurkite klase "KnygosBiblioteka", turincia atributa "knygos" (sarasa) ir metodus "prideti_knyga" ir
# "rodyti_knygas". Pridekite funkcionaluma, kad galetumete prideti knygas i sarasa ir atspausdinti visas bibl
# esancias knygas
# class KnygosBiblioteka:
#     def __init__(self):
#         self.knygos = []
#
#     def prideti_knyga(self, pavadinimas, autorius):
#         knyga = {
#             "pavadinimas": pavadinimas,
#             "autorius": autorius
#         }
#         self.knygos.append(knyga)
#         print(f"Knyga - {pavadinimas} sekmingai prideta!")
#
#     def rodyti_knygas(self):
#         if not self.knygos: # pasitikriname ar yra pridetu knygu
#             print("Knygu nerasta")
#         else:
#             print("Knygu sarasas:")
#             for knyga in self.knygos: # eina per visa musu sarasa ir tikrina kiekviena rakta - knyga
#                 print(f"Knygos pavadinimas: {knyga['pavadinimas']}, autorius: {knyga['autorius']}")
#
# knyga1 = KnygosBiblioteka()
#
# knyga1.prideti_knyga("Grybu karas", "Jurgis")
# knyga1.prideti_knyga("Uogu karas", "Vincas")
# knyga1.prideti_knyga("Vaisiu karas", "Antanas")
# knyga1.rodyti_knygas()
# funcijoje yra tik self (nera jokiu argumentu) todel tusti skliaustai ()

# 5. Sukurkite zodyna (dict = {}) su prekiu pavadinimais ir ju kainomis. Parasykite programa, kuri suskaiciuoja ir atspausdina
# visu prekiu kainu suma.
# prekiu_lentyna = {
#     "Obuolys": 0.55,
#     "Kriause": 0.33,
#     "Pienas": 0.99,
#     "Sultys": 1.99
# }
# print("Visu prekiu kainu suma:", sum(prekiu_lentyna.values()))

# 5. galima parasyti ir taip:
# prekiu_lentyna = {
#     "Obuolys": 0.55,
#     "Kriause": 0.33,
#     "Pienas": 0.99,
#     "Sultys": 1.99
# }
# suma = 0
# for kaina in prekiu_lentyna.values():
#     suma += kaina
#
# print(f"Visu prekiu kainu suma: {suma}")

# -------------------------------------------------------------------------------
# aukstis = 4
# eilutes = aukstis + 1
# for i in range(1, eilutes +1): #manipuliacija su eiluciu skaiciumi. iki galo nesuprantu
#     print(" " * (eilutes - i), end="") #
#     print("^" * (2 * i - 1))
#
# print(" " * (eilutes - 1), end="") # siuo atveju end="" perkelia i nauja eilute ir nurodo kur kuolas pasides
# # daugina tarpus is eilutes - 1 (kas yra 5-1 = 4). Po 4 tarpu ir padeda | (kamiena)
# print("|")


