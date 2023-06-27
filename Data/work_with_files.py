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
# filename = input("Iveskite naujo failo pavadinima-> ")
#
# try:
#     with open(filename, "w", encoding="utf8") as file:
#         file.write("Nera skirtumo koks lietuviškas tekstas")
#         print("Failas sukurtas sekmingai")
# except:
#         print("something went wrong!"


# -------------- 2023-06-26 paskaita -----------------
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees.csv')

# employees statistics
stats = df.agg({'SALARY': ['sum', 'mean', 'min', 'max', 'size']})
# print(stats)

# employees by JOB_ID
grouped_jobID = df.groupby('JOB_ID').agg({'SALARY': ['mean']})
# print(grouped_jobID)

# removing dublicates (neparasyta)
df.drop_duplicates()

# algos padidinimas (naujas stulpelis)
df['RAISED_SALARY'] = df.SALARY * 1.25
grouped_raised_salary = df.groupby('JOB_ID').agg({'RAISED_SALARY': ['mean']})
# print(grouped_raised_salary)

plt.bar(grouped_jobID, grouped_raised_salary)
plt.figure(figsize=(12, 10))

# grouped_raised_salary.plot(kind='line', figsize=(12, 10))
plt.title('Atlyginimas pagal profesiją')
plt.xlabel('Profesija')
plt.ylabel('Atlyginimas')

plt.show()



