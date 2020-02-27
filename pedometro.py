from microbit import *

#Define variable to record steps
steps = 0

while True:
    #Check to see if a steps has been taken.
    #If so, display a smile and increase the number of step
    if accelerometer.was_gesture('shake'):
        steps += 1
        display.show(Image.HAPPY)
        sleep(5000)
        display.clear()
    #Check to see if button A has been pressed
    #If so, display the number of steps taken
    if  button_a.is_pressed():
        #Check to see if number of steps is bigger
        if(steps > 9):
            display.scroll(str(steps))
            sleep(500)
            display.clear()
        #if number of steps is not bigger than 9
        else:
            display.show(str(steps))
            sleep(500)
            display.clear()
    if  button_b.is_pressed():
        steps = 0
        display.show(Image.HAPPY)
        display.clear()
