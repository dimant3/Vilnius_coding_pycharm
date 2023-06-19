
# def suma_nelyginiu(sarasas):
#     suma = 0
#     for nelyginis_skaicius in sarasas:
#         if nelyginis_skaicius % 2 != 0:
#             suma += nelyginis_skaicius
#     return suma
# pradinis_sarasas = [1,2,3,4,5,6,7,8,9,10]
# rezultatas = suma_nelyginiu(pradinis_sarasas)
# print(rezultatas)

# 3. 2023-06-13 Parašykite funkciją, kuri priima skaičių ir patikrina ar jis yra pirminis skaičius.
# def pirminis_skaicius (skaicius):
#     if skaicius < 2:
#         return False
#     for daliklis in range(2,skaicius):
#         if skaicius % daliklis == 0:
#             return False
#     return True
# skaicius = 100
# if pirminis_skaicius(skaicius):
#     print(f"skaicius {skaicius} yra pirminis")
# else:
#     print(f"skaicius {skaicius} nera pirminis")

# 2023-06-13 // FUNKCIJA WHILE //
## while funkcijos pvz(1)
# skaicius = 1
# while skaicius <= 5:
#     # tikrins tol kol kintamasis 'skaicius' bus maziau arba lygu 5
#     print(skaicius)
#     skaicius += 1

## while funkcijos pvz(2). Paprasom vartotojo ivesti skaiciu ir atspausdinti visus lyginius skaicius nuo ivesto
## skaiciaus iki 0!!!
# skaicius = int(input("Iveskite_skaiciu: "))
# while skaicius >= 0:
#     if skaicius % 2 == 0:
#         print(skaicius)
#     skaicius -= 1


# vardas = "Mantas"
# amzius = 15
# zodis = "Kaunas"
# miestai = ["Vilnius", "Kaunas", "Klaipeda"]
#
# if zodis in miestai:
#     print("Zodis "+ zodis + " egzistuoja sarase")
# else:
#     print("Zodis nerastas")
# print(len(miestai))

# skaicius = int(input("Iveskite skaiciu: "))
#
# if skaicius > 0:
#     print("Skaicius yra teigimas")
# elif skaicius < 0:
#     print("Skaicius yra neigiamas")
# else:
#     print("Skaicius yra nulis")

# print ("Mano vardas " + vardas + " As gyvenu " + miestai[0] + " mano amzius " + str(amzius))

# if amzius == 18:
#     print("Pilnametis")
# elif amzius >= 21:
#     print("Gali pirkti alų")
# else:
#     print("Nepilnametis")

# skaicius = -1
#
# if skaicius >= 0:
#     print("Skaicius yra teigiamas arba nulis")
# else:
#     print("Skaicius yra neigiamas")

# 2023-06-14 gale paskaitos teorijos
# DICTIONARY

# zmogus = {
#     "vardas": "Jonas",
#     "amzius": 27,
#     "miestas": "Vilnius"
# }
# print("Mano vardas: ", zmogus['vardas'])
#
#
# zmogus["lytis"] = "Vyras"
# # pridedame nauja elementa i savo zodyna
# print("As esu", zmogus["lytis"])
#
# # keiciame reiksmes
#
# zmogus["amzius"] = 20
#
# print("Atsiprasau man yra: ", zmogus['amzius'], "metu")
#
# # triname reiksmes
#
# del zmogus["miestas"]
# print(zmogus['miestas'])
#
# # iteruojame per visus zodyno elementus
# for key, value in zmogus.items():
#     print(key, ":", value)


# TUPLE - nekeiciamas, nekintamas objektas

# koordinates = (10,50)
# print(koordinates[0])
#
# koordinates1 = (54,42,12)
#
# sujungtos_koordinates = koordinates + koordinates1
# print(sujungtos_koordinates)

# 1. patikrinkite ar studentas islaike egzamina
# balas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# islaikymo_riba = 5
# balas = int(input("Iveskite gauta bala: "))
# if balas >= islaikymo_riba:
#     print("Egzaminas islaikytas")
# else:
#     print("Egzaminas neislaikytas")


# 2. Patikrinkite ar skaicius yra lyginis
# skaicius = 10
# if skaicius % 2 == 0:
     # apsirasoma, kad skaiciu dalinam is 2 ir liekana yra lygi 0. Nera liekanos po kablelio.
#     print("Lyginis skaicius")
# else:
#     print("Nelyginis skaicius")

# 3. Patikrinkite ar sąraše yra bent du skaičiai
# list = [13,18,23,25,26]
#
# if len(list) >= 2:
#     print("List has more than 2 records")
# else:
#     print("Less than 2 records")

# vardai = ["Jonas", "Saulius", "Lina", "Marius", "Rugile"]
#
# #   key(vardas) value(vardai)
# for vardas in vardai:
#     print(vardas)




##  1. Kaip atrinkti reikiamus skaicius is saraso
# skaiciai = [10,20,30,40,50,23]
# atrinkti = []
#
# for skaicius in skaiciai:
#     if skaicius > 25:
#         atrinkti.append(skaicius) # skaicius yra musu raktas
#
# print("Atrinkti skaiciai: ", atrinkti)

# 2. Isrinkti unikalius skaicius, kurie nepasikartoja
# skaiciai = [10, 10, 20, 44, 50, 50, 23, 23, 2, 45, 44, 11, 21]
# unikalios_reiksmes = []
#
# for skaicius in skaiciai:
#     if skaicius not in unikalios_reiksmes:
#         # not in panaikina pasiakrtojancias reikmes
#         unikalios_reiksmes.append(skaicius)
#
# print("Unikalios reikšmės: ", unikalios_reiksmes)


# FUNKCIJOS
# def suma(a, b):
#     return a + b
#
# rezultatas = suma(2, 5)
#
# print("Suma: ", rezultatas)

# def pasisveikinimas(vardas = "Anonimas"):
#     print("Labas,", vardas)
#
# pasisveikinimas("Mantas")

#Sarasu sujungimas, kai sarasus ivedame rezultatuose
# def sujungti_sarasus(sarasas1, sarasas2): #sukurem funkcija ir idejom 2 argumentus
#     sujungtas_sarasas = sarasas1 + sarasas2 #sukurem kintamaji jam priskyrem sukurtus argumentus
#     return sujungtas_sarasas #grazinam sujungtas_sarasas
#
# rezultatas = sujungti_sarasus([1,2,3],[4,5,6])
# #susikurem kita kintamaji, tuomet issikvieteme funkcija ir idejome 2 argumentus
# print("Sujungtas sarasas: ", rezultatas)


""""
4. Parasykite funkcija ar_lyginis, kuri priima viena skaiciu kaip argumenta ir patikrina ar skaicius yra lyginis. Jei
skaicius yra lyginis, tada funkcija turi grazinti True, o jei nelyginis - False.
"""
# def ar_lyginis(skaicius):
#     if skaicius % 2 == 0:
#         return True
#     else:
#         return False
# print(ar_lyginis(10))


# 5. Parasykite funkcija didziausias_skaicius, kuri priima sarasa skaiciu ir grazina didziausia skaiciu is saraso
# def didziausias_skaicius(sarasas):
#     didziausias = sarasas[0] # nulinis indeksas, nuo kurio pradedama tikrinti sarasas (0 atitinka pirma reiksme)
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias
# eina per visas reikšmes tikrindamas ir įsimindamas didžiausią reikšmę. 1 lygina su 8, 8 su 9 ir t.t.

# skaiciu_sarasas = [1, 8, 9, 55, 159, 1597, 8888, 9877]
# rezultatas = didziausias_skaicius(skaiciu_sarasas)
# print(rezultatas)

# 6. Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina naują sąrašą, kuriame yra tik unikalios
# reikšmės iš pradinio sąrašo.
# def unikalios_reiksmes(sarasas):
#     tuscias_sarasas = []
#     for reiksme in sarasas:
#         if reiksme not in tuscias_sarasas:
#             tuscias_sarasas.append(reiksme)
#             # append prideda reiksme i tuscia sarasa
#     return tuscias_sarasas
#
# naujas_sarasas = [5, 8, 15, 95, 48, 15, 95]
# print(unikalios_reiksmes(naujas_sarasas))
# unikalias reiksmes pridedam i nauja sarasa!




# 2023-06-16 paskaita!!!

# metodo perrasymas ir panaudojimas kitai klasei.
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def make_sound(self):
#         print("The animal makes a sound")
#
# class Dog(Animal):
#     def __init__(self, name, age): # kurdami nauja funkcija nurodome pasiimamus atributus ir sukuriamus.
#         super().__init__(name) # super() funkcija leidzia pasiimti is tevines klases atributa(name).
#         # galima pasiimti daugiau atributu tam paciam super.__init__(name, weigth, height) - pavyzdys.
#         self.age = age # sukuriamas naujas atributas.
#
#     def make_sound(self):
#         print("The dog barks")
#
# dog = Dog("Bob", 4)
# dog.make_sound()
# print(f"My dog name is {dog.name}" + " and age is " + str(dog.age))
# --------------------------------------------------------------------------


# Paveldimas metodas
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand
# # susikurem class su 1 atributu
#
#     def start_engine(self):
#         print("Engine started!")
#
#     def stop_engine(self):
#         print("Engine stopped")
#
# class Car(Vehicle):
#     #susikurem nauja klase ir paveldejom aukstesni - Vehicle ir papildomai sukureme drive funkcija
#     #dabar galim pasiimti is Vehicle class funkcijas ir sujunti su Car class funkcija.
#     def drive(self):
#         print("Car is driving!")
#
# car = Car("Toyota")
# print(car.brand)
# car.start_engine()
# car.drive()
# car.start_engine()
# ------------------------------------------------------------------------------------

# 1. sukurti class zmogus
# class Zmogus: # sukuriame tevine klase (pagrindine)
#     def __init__(self, name, age): #isvardiname savybes
#         self.name = name #aprasome savybes
#         self.age = age
#
#     def display_info(self): #METODAS rodyti informacija apie zmogu
#         print(f"Zmogaus vardas yra {self.name}")
#         print(f"Amzius yra {self.age}")
#
# class Darbuotojas(Zmogus): #Sukuriame vaikine (INHERITANCE) klase, kuri tures rysi su pagrindine.
#     def __init__(self,name, age, salary): #Isvardiname kokias savybes tures darbuotojas
#         super().__init__(name, age)     # nurodome, kurias savybes paveldes is Zmogus klases
#         self.salary = salary            # aprasome papildoma savybe
#
#     def display_info(self):
#         super().display_info() # panaudosiu tevines klases funkcija display_info esanti virsuje prie Zmogus class.
#         print(f"Darbuotojo atlyginimas yra {self.salary}") #zmogus klase neturi atlyginimo atributo
#
# zmogus = Zmogus("Antanukas", 16)                #sukuriame tevines klases(Zmogus) objekta (zmogus)
# darbuotojas = Darbuotojas("Vincas", 50, 3500)   #sukuriame vaikines klases(Darbuotojoas) objekta.
#
# zmogus.display_info()
# print() # tuscias print padaro tarpa tarp rezultatu.
# darbuotojas.display_info()

# --------------------------------------------------------------------------------

# 2. Sukurti pirkiniu krepselio funkcionaluma. Turim produkta ir turim krepseli.

# class Product:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#     def display_info(self):
#         print(f"Produktas: {self.title}, kaina: {self.price} €") #pabandysiu viena eilute
#
# class DiscountedProduct(Product):
#     def __init__(self, title, price, discount_percentage):
#         super().__init__(title, price)
#         self.discount_percentage = discount_percentage
#
#     def calculated_discounted_price(self):
#         discount_amount = self.price * (self.discount_percentage / 100) # metoduose visuomet self
#         discounted_price = self.price - discount_amount # kai naudoji savybes nereikia self
#         return discounted_price
#
#     def display_info(self):
#         super().display_info() # pasiimam metoda is tevines klases.
#         print(f"Nuolaida {self.discount_percentage} %")
#         print(f"Galutine kaina: {self.calculated_discounted_price()} €")
#
# class ShoppingCart(Product): # klases pavadinime underscore vengiame. Capital letters
#     def __init__(self):
#         super().__init__(title=None, price=None) # cia pasikomentuoti
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#         print(f"Produktas {product.title} pridetas i krepseli.")
#
#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#             print(f" Produktas {product.title} pasalintas is krepselio.")
#         else:
#             print(f" Produktas {product.title} nerastas krepselyje.")
#
#     def calculate_total_price(self):
#         total_price = 0
#         for product in self.products:
#             total_price += product.price
#         return total_price  # for ciklas visada pasibaigia return.
#
#
#
# prod1 = Product("Pienas", 2.99) # cia daugiau nieko nereikia, nes Product turi 2 reiksmes
# prod2 = DiscountedProduct("Obuolys", 1.99, 15) # gale rasosi nuolaida 15
# prod3 = Product("Sviestas", 3.99)
#
# cart = ShoppingCart()
# cart.add_product(prod1)
# cart.add_product(prod2)
# cart.add_product(prod3)
# print()
# for product in cart.products:
#     product.display_info()
#     print()
#
# total_price = cart.calculate_total_price()
# print(f"Bendra krepselio kaina: {total_price} €")
# print()
#
# cart.remove_product(prod1)
# print()
#
# total_price = cart.calculate_total_price()
# print(f"Nauja krepselio kaina: {total_price} €")

# random funkcija paleista + importuotas laikmatis, kada ismeta rezultata.
# import random
# import time
# studentai = ["Rugile", "Egidijus", "Deividas", "Tomas","Migle","SauliusS", "SauliusA", "Aušrinė", "Mantas", "Vaidas",
#              "Juratė", "Modestas"]
# random_student = random.choice(studentai)
# time.sleep(3)
# print("Atsitiktinai pasirinktas studentas: ", random_student)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self): #get gaunam reiksmes
#         return self.name #nebuvome apsibrezia todel self
#
#     def set_name(self, name): #set nustatom reiksmes
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         if age >= 0:
#             self.age = age
#         else:
#             print("Amzius negali buti neigiamas!")
#
# person = Person("Julius", 20)
#
# print("name", person.get_name()) #person.get_name() yra metodas todel papildomi skliaustai
# print("age", person.get_age())
#
# person.set_name("Virgis")
# person.set_age(33)
#
# print("new_name", person.get_name())
# print("new_age", person.get_age())

