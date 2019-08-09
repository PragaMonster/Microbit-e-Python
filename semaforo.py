from microbit import * #estamos importando a biblioteca python microbit
while True:
    pin0.write_digital(1) #led red
    sleep(5000)
    pin0.write_digital(0)
    pin2.write_digital(1) #led green
    sleep(5000)
    pin2.write_digital(0)
    pin1.write_digital(1) #led yellow
    sleep(2000)
    pin1.write_digital(0)
    