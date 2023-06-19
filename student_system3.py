print("------ STUDENTU VALDYMO SISTEMA ------")

# Create class "StudentsSystem" (sukuriama klase)
class StudentsSystem:
    # Constructor
    def __init__(self):
        self.students = [] # sukuriamas tuscias sarasas, kuris pildysis

    def add_student(self): # prideti studenta funkcija
        id = input("Iveskite naujo studento id -> ") #input
        if id.isnumeric(): # salyga, patikrinti kad neivestu to pacio id
            id = int(id)
            for students1 in self.students:
                if students1["id"] == id:
                    print("Toks ID jau egzistuoja")
                    return
            name = input("Iveskite varda: ")
            last_name = input("Iveskite studento pavarde: ")
            age = input("Iveskite studento amziu: ")
            studentas = {
                "id": id,
                "name": name,
                "last_name": last_name,
                "age": age
            }
            self.students.append(students1) # pridedamas i sarasa kintamasis students1
        else:
            print("id turi buti tik skaicius!")

    def remove_student(self):
        id = int(input("Iveskite studento id: "))
        for stud in self.students:
            if stud["id"] == id:
                self.students.remove(stud)
                print(f"Irasas {stud['id']} sekmingas pasalintas!")
                return
        print(f"Tokio studento {id} nera sarasuose")

    def display_info_1(self):
        id = int(input("Iveskite studento id: "))
        for stud in self.students:
            print(stud["id"])
            if stud["id"] == id:
                print(f"Informacija apie studenta: ")
                print(f"id: {stud['id']}")
                print(f"id: {stud['name']}")
                print(f"id: {stud['last_name']}")
                print(f"id: {stud['age']}")
                return
        print("Studento nera sarase")

    def full_list(self):
        print(f"Studentu sarasas: {self.students}")
        for stud in self.students:
            print(f"Studentu sarasas: ")
            print(f"id: {stud['id']}")
            print(f"id: {stud['name']}")
            print(f"id: {stud['last_name']}")
            print(f"id: {stud['age']}")

system = StudentsSystem
while True:
    print("Pasirinkite norima veiksma->")
    print("1. Ivesti nauja studenta")
    print("2. Pasalinti studenta is saraso")
    print("3. Perziureti informacija apie studenta")
    print("4. Perziureti visu studentu sarasa")
    print("0. Uzbaigti pasirinkimus")
    pasirinkimas= input("Iveskite pasirinkimo numeri_-> ")
    if pasirinkimas == "1":
        system.add_student()
    elif pasirinkimas == "2":
        system.remove_student()
    elif pasirinkimas == "3":
        system.display_info_1()
    elif pasirinkimas == "4":
        system.full_list()
    elif pasirinkimas == "0":
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar karta")
