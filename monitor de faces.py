from microbit import *
Sad = 0 #B
Happy = 0 #A
Silly = 0 #WHITE
Angry = 0 #BLUE

while True:
    button_blue = pin1.read_digital()
    button_white = pin0.read_digital()
    if button_a.is_pressed():
        display.show (Image.HAPPY)
        sleep(2000)
        display.clear()
        Happy += 1
        if (Happy <= 9):
            display.show(str(Happy))
            sleep(2000)
        else:
            display.scroll(str(Happy))
            sleep(2000)
        display.clear()#FIM HAPPY
    if button_b.is_pressed():
        display.show(Image.SAD)
        sleep(2000)
        display.clear()
        Sad += 1
        if(Sad <= 9):
            display.show(str(Sad))
            sleep(2000)
        else:
            display.scroll(str(Sad))
            sleep(2000)
        display.clear()
    if button_blue == (1):
        display.show (Image.ANGRY)
        sleep(2000)
        display.clear()
        Angry += 1
        if(Angry <= 9):
            display.show(str(Angry))
            sleep(2000)
        else:
            display.scroll(str(Angry))
            sleep(2000)
        display.clear() #FIM angry
    if button_white == (1):
        display.show (Image.SILLY)
        sleep(2000)
        display.clear()
        Silly += 1
        if(Silly <=9):
            display.show(str(Silly))
            sleep(2000)
        else:
            display.scroll(str(Silly))
            sleep(2000)
        display.clear()
#FIM silly
    if button_white == 1 and button_blue == 1:
        display.show(Image.ANGRY)
        sleep(2000)
        display.scroll(str(Angry))
        sleep(2000)
        display.show(Image.HAPPY)
        sleep(2000)
        display.scroll(str(Happy))
        sleep(2000)
        display.show(Image.SILLY)
        sleep(2000)
        display.scroll(str(Silly))
        sleep(2000)
        display.show(Image.SAD)
        sleep(2000)
        display.scroll(str(Sad))
        sleep(2000)
