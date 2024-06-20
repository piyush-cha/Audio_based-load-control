import RPi.GPIO as GPIO
import speech_recognition as sr
import pyaudio

# GPIO setup
relay_pin = 17  # Use the appropriate GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, GPIO.HIGH)

# Initialize recognizer
recognizer = sr.Recognizer()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None

def control_load(command):
    if "turn on" in command:
        GPIO.output(relay_pin, GPIO.LOW)
        print("Load turned ON")
    
    elif "turn off" in command:
        GPIO.output(relay_pin, GPIO.HIGH)
        print("Load turned OFF")
    
    else:
        print("Command not recognized")

try:
    while True:
        command = listen_for_command()
        if command:
            control_load(command)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()
