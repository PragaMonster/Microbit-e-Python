from microbit import *
import music

analog_2 = 0
counter = 0
previous_running_time = 0
target = 20000
remind = 0

while True:

    current_running_time = running_time()
    analog_2 = pin2.read_analog()
    print(analog_2)
    sleep(20)

    if (remind == 0):
        if (analog_2 >= 500):
            display.show(Image.HEART)
            music.play("C5:2")
            counter = counter + 1
            remind = 1

    if(remind == 1):
        if(analog_2 < 500):
            display.clear()
            remind = 0

    if((current_running_time - previous_running_time) >= target):
        counter = counter * 3
        display.scroll("%d bpm" % (counter),delay=100,)
        counter = 0
        previous_running_time = running_time()
    print(("{},{})".format(analog_2,counter))

