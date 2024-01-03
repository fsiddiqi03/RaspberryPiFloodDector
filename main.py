import RPi.GPIO as GPIO
# import time

# GPIO pin number where the sensor is connected
SENSOR_PIN = 17  # Replace with your specific GPIO pin number

GPIO.setmode(GPIO.BCM)  # BCM pin numbering
GPIO.setup(SENSOR_PIN, GPIO.IN)  # Set the sensor pin as input

try:
    while True:
        num = GPIO.input(SENSOR_PIN)
        print(num)

except KeyboardInterrupt:
    GPIO.cleanup()
