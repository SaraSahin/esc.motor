from time import sleep
import pigpio
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pi = pigpio.pi()
# Calibrate ESC
ESC_GPIO = 13

pi.set_servo_pulsewidth(ESC_GPIO, 1200) # Maximum throttle.
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1000) #Maximun throttle.
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1300) #Maximum throttle.
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1000) #Maximum throttle.
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1100) #Maximum throttle.
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1000) #Maximum throttle.
sleep(2)