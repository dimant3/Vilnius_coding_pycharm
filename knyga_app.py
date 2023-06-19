
# class Knyga:
#     def __init__(self, pavadinimas, autorius, puslapiai):
#         self.pavadinimas = pavadinimas
#         self.autorius = autorius
#         self.puslapiai = puslapiai
#         #zemiau parasome metoda, kuris tikrina ar knyga turi > 300 psl
#     def virs_300_psl(self):
#         if self.puslapiai > 300:
#             return True
#         else:
#             return False
#
# # sukuriame objekta
# Knyga1 = Knyga("Haris Porteris", "Dumbldoras", 600)
# Knyga2 = Knyga("Grybu karas", "Jonas Grybas", 250)
#
# print(Knyga1.virs_300_psl())
# print(Knyga2.virs_300_psl())

# class Darbuotojas:
#     def __init__(self, vardas, pavarde, atlyginimas):
#         self.vardas = vardas
#         self.pavarde = pavarde
#         self.atlyginimas = atlyginimas
#         # parasyti metoda, kuris padidins darbuotoju atlyginima tam tikru %
#     def padidinti_atlyginima(self, procentai):
#         padidinimas = self.atlyginimas * procentai / 100
#         self.atlyginimas += padidinimas
#         #def kuris pakeis pavarde
#     def pakeisti_pavarde(self, nauja_pavarde):
#         self.pavarde = nauja_pavarde
#         print("Pavarde pakeista sekmingai")
#     def visa_informacija(self):
#         print(f"Informacija apie darbuotoją: ")
#         print(f"Vardas: {self.vardas}")
#         print(f"Pavardė: {self.pavarde}")
#         print(f"Atlyginimas: {self.atlyginimas}")

# sukuriame objekta
# Darbuotojas1 = Darbuotojas("Jonas", "Jonaitis", 1800)
# Darbuotojas2 = Darbuotojas("Virginijus", "Seskus", 2500)

# Darbuotojas1.padidinti_atlyginima(10)
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} naujas atlyginimas: {Darbuotojas1.atlyginimas}")
# Darbuotojas1.pakeisti_pavarde("Kazlauskas")
# print(f"{Darbuotojas1.vardas} {Darbuotojas1.pavarde} pavarde pakeista!")
# Darbuotojas1.visa_informacija()

# Darbuotojas2.padidinti_atlyginima(20)
# print(f"{Darbuotojas2.vardas} {Darbuotojas2.pavarde} naujas atlyginimas: {Darbuotojas2.atlyginimas}")

# class Preke:
#     def __init__(self, pavadinimas, kaina, kiekis):
#         self.pavadinimas = pavadinimas
#         self.kaina = kaina
#         self.kiekis = kiekis
#         # parasyti metoda, kad galetume atnaujinti kaina
#     def atnaujinti_kaina(self, nauja_kaina):
#         self.kaina = nauja_kaina
#         print(f"{self.pavadinimas} nauja kaina: {nauja_kaina}")
#     def sandelio_likutis(self, pardavimo_kiekis):
#         # reikia pranesti pirkejui, kad sandelyje nera tiek prekiu
#         if pardavimo_kiekis <= self.kiekis:
#             self.kiekis -= pardavimo_kiekis
#             print(f"Parduota {self.pavadinimas} {pardavimo_kiekis}")
#         else:
#             print(f"Nepakanka prekiu: {self.pavadinimas}")
#     def sandelio_papildymas(self, padidintas_likutis):
#         self.kiekis += padidintas_likutis
#         print(f"Padidintas kiekis {self.pavadinimas} {padidintas_likutis}")
#
# #sukuriamas objektas
# Preke1 = Preke("Obuolys", 2, 10)
# Preke2 = Preke("Sokoladas", 3, 5)
#
# Preke1.atnaujinti_kaina(3)
# Preke1.sandelio_likutis(15)
# Preke2.sandelio_likutis(8)
# Preke1.sandelio_papildymas(20)
# Preke2.sandelio_papildymas(15)
# print("Sandelio likutis", Preke1.kiekis)

# ------------------------ BLOGO KURIMAS --------------------

class Blog:
    def __init__(self):
        self.posts = []

    def create_post(self, pavadinimas, aprasymas):
        post = {
            "pavadinimas": pavadinimas,
            "aprasymas": aprasymas
        }
        self.posts.append(post)
        print("Irasas sekmingai sukurtas")

    def display_all_posts(self):
        if not self.posts:
            print("No blog posts found")
        else:
            print("Blog posts: ")
            for post in self.posts:
                print(f"Title: {post['pavadinimas']} ")
                print(f"Description: {post['aprasymas']}")
                print("__________")
    def update_post(self, pavadinimas, naujas_aprasymas):
        for post in self.posts:
            if post["pavadinimas"] == pavadinimas: # cia yra salyga, todel turi buti dvigubas ==
               post["aprasymas"] = naujas_aprasymas # cia yra prilyginimas, todel vienas =
               print("Blog post updated!")
               break
        else:
            print("Blog post not found")

    def delete_post(self, pavadinimas):
        for post in self.posts:
            if post ["pavadinimas"] == pavadinimas:
                self.posts.remove(post)
                print("Blog post deleted!")
                break
        else:
            print("Blog post not found")


post1 = Blog()
post1.create_post("Duomenu analitikos studentai uzkariavo pasauli", "Python, SQL, Power BI")
post1.create_post("Kulinarijos sedevrai", "Saldus gaminiai per 30minuciu")
post1.create_post("Kodel yra todel?", "Nesuprantamu ivykiu paaiskinimas")
#post1 visur naudojam todel, kad objekta naudojam ta pati, kuris neturi atributu.
post1.update_post("Kodel yra todel?", "Papildyta pora nauju istoriju apie paaiskinimus")
post1.display_all_posts()
post1.delete_post("Kodel yra todel?")
post1.display_all_posts()