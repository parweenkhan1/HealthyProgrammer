from pygame import mixer
from datetime import datetime
from time import time

def song_in_loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log(msg):
    with open("../Snake/my_log.txt", "a")as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    #songinloop("","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_secs = 60*30
    eyes_secs = 60*60*4
    exercise_secs = 2*60*60
    while True:
        if time()-init_water > water_secs:
            print("Now lets drink water, and write stop_drinking to stop the alarm")
            song_in_loop("Drinking-Water-www.fesliyanstudios.com.mp3", "stop_drinking")
            init_water = time()
            log("drank water at")
        if time()-init_eyes > eyes_secs:
            print("Now lets do some to relax eyes, and write done_eyes to stop the alarm")
            song_in_loop("Hazards-Blinking-W-Medium-Mic-FesliyanStudios.com.mp3", "done_eyes")
            init_eyes = time()
            log("eyes relaxed at")
        if time()-init_exercise > exercise_secs:
            print("Now lets do some exercise to relax our muscles, and write done_exercise to stop the alarm")
            song_in_loop("sneaker-shoe-on-concrete-floor-fast-pace-1-www.FesliyanStudios.com.mp3", "done_exercise")
            init_exercise = time()
            log("done with exercise at")

    f.close()