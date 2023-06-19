import random
# import random module // built-in Python no installation

# nurodoma iki kokio skaiciaus bus spejama
top_of_range = input("Type a number: ")

if top_of_range.isdigit(): # tikrina ar ivestas simbolis yra skaicius
    top_of_range = int(top_of_range) #jeigu skaicius, paverciame ji integer

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number larger than 0 next time")
    quit()


random_number = random.randint(0, top_of_range)
#sioje vietoje paims ivesta top_of_range reiksme ir nurodome sekos pradzia 0.
guesses = 0 #pridedam spejimu kintamaji ir priskiriam 0 reiksme.

while True:
    guesses += 1
    # ivestas pirmas spejimas bus 1 ir kiekviena karta kol kartosis ciklas (continue) prisides po 1 spejima
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        # tikrina ar ivestas simbolis yra skaicius
        user_guess = int(user_guess) #jeigu skaicius, paverciame ji integer
    else:
        print("Please type a number next time.")
        continue # jeigu neteisingai ivestas, continue grazina i pradzia while.

    if user_guess == random_number: # jeigu spejimas sutampa su random sugeneruotu skaicium
        print("You got it!")
        break # break po sito if sustabdo cikla
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")


print("You got it in", guesses, "guesses")