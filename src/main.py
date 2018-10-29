import ASUS.GPIO as GPIO
import time

# BOARD MODE
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
p = GPIO.PWM(7, 0.01)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
p1 = GPIO.PWM(23, 0.01)

while True:
  GPIO.output(3, GPIO.HIGH)
  GPIO.output(5, GPIO.LOW)
  GPIO.output(21, GPIO.HIGH)
  GPIO.output(19, GPIO.LOW)
  p.start(100)
  p1.start(100)
