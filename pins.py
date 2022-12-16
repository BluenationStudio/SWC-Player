import RPi.GPIO as GPIO
from omxplayer import OMXPlayer
from time import sleep
from pathlib import Path

# GPIO pin number :
light = 7

# Setup the player as shown in omxplayer-wrapper examples :
path = Path('./video.mp4')

# the on and off times in seconds
on_target = 1
off_target = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(light, GPIO.OUT)
player = OMXPlayer(path, args=['--no-osd', '--blank'])
player.pause()
sleep(5)
player.play()

# Make a query to position() inside infinite loop 
while (1):
    try:
        position = int(player.position())
    except:
        # You will get an OMXPlayerDeadError eventually
        break
    if position >= on_target and position <= off_target:
        GPIO.output(light, GPIO.HIGH)
        print("This is where the first GPIO should be triggered")
    # Check position again in one second. 
    # sleep works, but you might want to find an alternative
    sleep(1)

player.quit()