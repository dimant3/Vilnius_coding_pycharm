
# Darbas su failais naudojant open funkcija:

# file = open("tekstas.txt", "a", encoding="utf8")
# file.write("nesvarbu koks tekstas, dar prisideda lietuviškų simbolių")
# file.close() # close baigia veiksma
# "r" - read file
# "w" - write file - iraso reiksmes
# "a" - append file - jeigu jau failas egzistuoja ir yra turinys, tai tas turinys bus papildytas.
# encoding="utf8" - rodo lietuviskus simbolius.

# --------- with open funkcija -----------------

# with open("tekstas1.txt", "w", encoding="utf8") as file:
#     file.write("Tekstas antrajame faile\n")
#     file.write("Antra eilute teksto\n")
#     file.write("Trecia eilute teksto\n")

# ------- file read with try / except ---------------
# filename = input("Iveskite failo pavadinima-> ")

# try:
#     with open(filename, "r", encoding="utf8") as file:
#         content = file.read()
#         print("File content: ")
#         print(content)
# except FileNotFoundError:
#     print("File not found") # tokio failo nera
# except:
#     print("something went wrong!") # jeigu failo nepavyksta nuskaityti, nors faila rado.

# ------- file write with try / except -------------
filename = input("Iveskite naujo failo pavadinima-> ")

try:
    with open(filename, "w", encoding="utf8") as file:
        file.write("Nera skirtumo koks lietuviškas tekstas")
        print("Failas sukurtas sekmingai")
except:
        print("something went wrong!")