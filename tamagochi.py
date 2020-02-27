from microbit import *
import random
INTERVAL = 5000

RIGHT = Image(
    "90900:"
    "00000:"
    "00000:"
    "90009:"
    "09990:")

LEFT = Image(
    "00909:"
    "00000:"
    "00000:"
    "90009:"
    "09990:")

MOUTH_OPEN = Image(
    "09090:"
    "00000:"
    "09990:"
    "09990:"
    "90009:")

MOUTH_CLOSED = Image(
    "09090:"
    "00000:"
    "00000:"
    "09990:"
    "00000:")

SLEEP = Image(
    "99099:"
    "00000:"
    "00000:"
    "09990:"
    "00000:")

class Game():
    def __init__(self):
        self.last = None
        self.x_pos = 0
        self.y_pos
        display.scroll ("Catch the ball")

    def draw(self):
        image = Image(
            "00000:"
            "00000:"
            "00500:"
            "00000:"
            "00000:")
        image.set_pixel(self.x_pos, self.y_pos,9)
        display.show(image)

    def start(self):
        while True:
            self.check_win()
            self.check_direction()
            if button_a.is_pressed():
                break
            if button_b.is_pressed():
                break

    def make_new_spot(self):
        self.x_pos = random.randrange(5)
        self.y_pos = random.randrange(5)
        if self.x_pos == 2 and self.y_pos == 2:
            self.x_pos = 4
            self.y_pos = 4

    def check_win(self):
        if self.x_pos == 2 and self.y_pos == 2:
            display.show(Image.HEART)
            sleep(2000)
            self.make_new_spot()
            self.draw()

    def check_direction(self):
        gesture = accelerometer.current_gesture()
        if gesture == self.last:
            return
        if gesture == "up":
            if self.y_pos < 4:
                self.y_pos += 1
        elif gesture == "down":
            if self.y_pos > 0 :
                self.y_pos -=1
        elif gesture =="left":
            if self.x_pos > 0 :
                self.x_pos -=1
        elif gesture =="right":
            if self.x_pos < 4:
                self.x_pos +=1
        else:
            return
        self.last = gesture
        self.last()

class Pet(object):
    def __init__(self):
        self.last_time = 0
        self.happy()
        self.action = False
        self.bgl = 6.5

    def happy(self):
        display.show(Image.HAPPY)
        self.action = False

    def angry(self):
        display.show(Image.ANGRY)
        self.action = False

    def asleep(self):
        display.show(Image.SLEEP)
        self.action = False

    def surprised(self):
        display.show(Image.SURPRISED)
        self.action = True
        if self.bgl > 4:
            self.bgl -=0.1

    def tick(self):
        if self.bgl >0:
            self.bgl -=0.1
        self.set_face()

    def set_face(self):
        if self.bgl < 4 :
            self.sad()
        elif self.bgl > 8:
            self.asleep()
        else:
            self.happy()

    def check_gesture(self):
        gesture = accelerometer.current_gesture()
        if gesture == "shake":
            self.surprised()
            sleep(1000)
        elif gesture == "face down":
            display.show(Image.CONFUSED)
            self.action = True
        elif gesture == "left":
            display.show(LEFT)
            self.action = True
        elif gesture =="right":
            display.show(RIGHT)
            self.action = True
        else:
            if self.action:
                self.set_face()

    def check_button(self):
        if button_a.is_pressed() and button_b.is_pressed():
            self.play()
        elif button_a.is_pressed():
            self.bgl += 1
            display.show(
                [MOUTH_OPEN,MOUTH_CLOSED,MOUTH_OPEN,MOUTH_CLOSED],
                300)
            self.set_face()
        elif button_b.is_pressed():
            display.scroll("{0:0.1f}".format(self.bgl))

    def check_death(self):
        if self.bgl < 1:
            display.show(Image.SKULL)
            return True
        elif self.bgl > 30:
            display.show(Image.GHOST)
            return True
        return False

    def wait(self):
        while True:
            if self.check_death():
                break
            self.check_gesture()
            self.check_button()
            current = running_time()
            delta = current - self.last_time
            if delta > INTERVAL:
                self.last_time = current
                self.tick()

    def play(self):
        game = Game()
        game.start()

if __name__ == '__main__':
    PET = Pet()
    PET.wait()


