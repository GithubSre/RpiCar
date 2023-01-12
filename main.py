from MotorModule import Motor
import KeyboardModule as kb

#################################################################################
motor = Motor(2, 3, 4, 22, 17, 27)
#################################################################################

kb.init()

def main():
    if kb.getKey('UP'):
        motor.move(0.6, 0, 1)
    elif kb.getKey('DOWN'):
        motor.move(-0.6, 0, 1)
    elif kb.getKey('LEFT'):
        motor.move(0.3, -0.3, 1)
    elif kb.getKey('RIGHT'):
        motor.move(0.3, 0.3, 1)
    else:
        motor.stop()

if __name__ == '__main__':
    while True:
        main()
