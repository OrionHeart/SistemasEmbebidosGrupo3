import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while 1:
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(17, GPIO.LOW)

GPIO.cleanup()