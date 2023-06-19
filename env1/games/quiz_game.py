print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes": # norim tik yes atsakymo, kitu atveju quit
    # playing.lower() visur pridedam, kad panaikintume ivestas reikmes case sensitive (reiksmes bus traktuojamos kaip
    # lower. Ta pati pritaikome ir zemiau ivedamiems atsakymams.
    quit()

print("Let's do it :)")
score = 0
# surinkti balai prasideda nuo 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1 # pridedamas 1 balas.
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1  # pridedamas 1 balas.
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1  # pridedamas 1 balas.
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1  # pridedamas 1 balas.
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str((score/4) * 100) + "%") # 4 yra klausimu skaicius
# your total score : score