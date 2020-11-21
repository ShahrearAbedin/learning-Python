
# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from datetime import datetime
from time import time
import pyttsx3
manager = pyttsx3.init()
voices = manager.getProperty('voices')
manager.setProperty('voice', voices[1].id)
newVoiceRate = 125
manager.setProperty('rate', newVoiceRate)

exercise = "It is time for physical activity. Please hurry up. Don't be lazy. Inform me after you're done."
eye = "Time for eye exercise. Please don't forget it. It will reduce your eye strain. Please inform me after ending."
water = "Water time! You should drink water. It's important for your health. Please inform me after finishing."
congrats = "Congrats. You have completed your task. Thanks a lot."

def managerloop(file, stopper):
    manager.say(file)
    manager.runAndWait()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            manager.say(congrats)
            manager.runAndWait()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"Shahrear Abedin:- {msg} {datetime.now()}\n")

init_water = time()
init_eyes = time()
init_exercise = time()
watersecs = 40*60
exsecs = 50*60
eyessecs = 30*60

while True:
    if time() - init_water > watersecs:
        print("Water Drinking time. Enter 'done' to inform her.")
        managerloop(f'{water}', 'done')
        init_water = time()
        log_now("Drank Water at")

    if time() - init_eyes >eyessecs:
        print("Eye exercise time. Enter 'done' to inform her.")
        managerloop(f'{eye}', 'done')
        init_eyes = time()
        log_now("Eyes Relaxed at")

    if time() - init_exercise > exsecs:
        print("Physical Activity Time. Enter 'done' to inform her.")
        managerloop(f'{exercise}', 'done')
        init_exercise = time()
        log_now("Physical Activity done at")
