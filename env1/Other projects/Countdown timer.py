import time
# imported time libabry

def countdown(time):
    while time:
        mins, secs = divmod(time, 60)
        # divmod - euclidean division where time (kintamasis) is divided by 60
        timer = '{:02d}:{:02d}'.format(mins, secs) # kazkoks timer formatavimo nurodymas
        print(timer, end="\r")
        time -= 1
        time.sleep(1)
    print('GO for a run!')

time = input("Enter the time in seconds: ")

countdown(int(time))
# funkcijos iskvietimas
# countdown funcijoje time naudojom kaip str, kad isventi klaidu konvertuojam i integer.