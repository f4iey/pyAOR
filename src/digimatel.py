# List of functions and shortcuts for DIGIMATEL Keyboard
import os
import keyboard
import serial
import pyttsx3
from Commands import *

class Digimatel:
    def __init__(self):
        self.command = Commands()
        self.ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'french+f4')
        self.engine.setProperty('rate', 150)
        self.inputk = self.record_keyboard_input()

    def get_freq_mode(self):
        self.command.rf.send(self.ser)
        self.command.rf.response(self.ser, self.engine)
        self.command.md.send(self.ser)
        self.command.md.response(self.ser, self.engine)
    def numlock(self):
        self.engine.say("Verouillage numérique")
        self.engine.runAndWait()
    def minus(self):
        self.engine.say("Commande annulée")
        self.engine.runAndWait()

    def record_keyboard_input(self):
        recorded_text = ""

        while True:
            try:
                event = keyboard.read_event()
                if event.event_type == keyboard.KEY_DOWN:
                    # Append the pressed key to the recorded_text string
                    recorded_text += event.name
                    # If Enter key is pressed, break the loop and stop recording
                    if event.name == "enter":
                        if recorded_text == "enter":
                            self.get_freq_mode()
                            recorded_text = ""
                            continue
                        elif recorded_text.find('.') and len(recorded_text[0:len(recorded_text)-5]) <= 10:
                            recorded_text = recorded_text[0:len(recorded_text)-5]
                            # filling zeros
                            for i in range(10 - len(recorded_text)):
                                recorded_text = '0' + recorded_text
                            # removing decimal point
                            recorded_text.replace('.', '')
                            # place decimal point to the center of the string to send
                            recorded_text = recorded_text[0:len(recorded_text)//2] + '.' + recorded_text[len(recorded_text)//2:]
                            # send
                            self.rf.send_param(self.ser, recorded_text)
                            self.engine.say("OK, mode VFO")
                            self.engine.runAndWait()
                            continue
                        match(recorded_text):
                            case "00enter":
                                #Auto
                                self.command.md.send_param(self.ser, "000")
                                self.engine.say("OK, Décodage Automatique")
                                self.engine.runAndWait()
                            case "01enter":
                                #USB
                                self.command.md.send_param(self.ser, "004")
                                self.engine.say("OK, USB")
                                self.engine.runAndWait()
                            case "02enter":
                                #LSB
                                self.command.md.send_param(self.ser, "005")
                                self.engine.say("OK, LSB")
                                self.engine.runAndWait()
                            case "03enter":
                                #CW
                                self.command.md.send_param(self.ser, "006")
                                self.engine.say("OK, CW")
                                self.engine.runAndWait()
                            case "04enter":
                                #FM30
                                self.command.md.send_param(self.ser, "0F0")
                                self.command.ifn.send_param(self.ser, "2")
                                self.command.ifn.response(self.ser, self.engine)
                                self.engine.say("OK, FM")
                                self.engine.runAndWait()
                            case "05enter":
                                #FM15
                                self.command.md.send_param(self.ser, "0F0")
                                self.engine.say("OK, FM")
                                self.engine.runAndWait()
                            case "06enter":
                                #FM6
                                self.command.md.send_param(self.ser, "0F0")
                                self.command.ifn.send_param(self.ser, "4")
                                self.command.ifn.response(self.ser, self.engine)
                                self.engine.say("OK, FM")
                                self.engine.runAndWait()
                            case "07enter":
                                #WFM
                                self.command.md.send_param(self.ser, "0F0")
                                self.command.ifn.send_param(self.ser, "1")
                                self.command.ifn.response(self.ser, self.engine)
                                self.engine.say("OK, WFM")
                                self.engine.runAndWait()
                            case "08enter":
                                #AM
                                self.command.md.send_param(self.ser, "001")
                                self.engine.say("OK, A aime")
                                self.engine.runAndWait()
                            case "09enter":
                                #DSTAR
                                self.command.md.send_param(self.ser, "110")
                                self.engine.say("OK, D-STAR")
                                self.engine.runAndWait()
                            case "*4enter":
                                # Niveau de volume 1
                                os.system("pactl set-sink-volume 0 25%")
                                self.engine.say("OK, Niveau 1")
                                self.engine.runAndWait()
                            case "*44enter":
                                # Niveau de volume 1
                                os.system("pactl set-sink-volume 0 50%")
                                self.engine.say("OK, Niveau 2")
                                self.engine.runAndWait()
                            case "*444enter":
                                # Niveau de volume 1
                                os.system("pactl set-sink-volume 0 75%")
                                self.engine.say("OK, Niveau 3")
                                self.engine.runAndWait()
                            case "*4444enter":
                                # Niveau de volume 1
                                os.system("pactl set-sink-volume 0 95%")
                                self.engine.say("OK, Niveau 4")
                                self.engine.runAndWait()

                            case _:
                                self.engine.say("Commande inconnue")
                                self.engine.runAndWait()
                        recorded_text = ""
                    elif event.name == "-":
                        self.minus()
                        recorded_text = ""
                    else:
                        self.engine.say(event.name)
                        self.engine.runAndWait()
            except KeyboardInterrupt:
                # Exit the loop if Ctrl+C is pressed
                break

        return recorded_text
