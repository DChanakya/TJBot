import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
pwm=GPIO.PWM(3,50)

pwm.start(6)
time.sleep(9)
pwm.ChangeDutyCycle(1)
time.sleep(1)
pwm.stop()

GPIO.cleanup()
