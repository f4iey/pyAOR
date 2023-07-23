# List of functions and shortcuts for DIGIMATEL Keyboard
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
                        match(recorded_text):
                            case "00enter":
                                #Auto
                                self.command.md.param = "000"
                                self.command.md.send(self.ser)
                                self.engine.say("OK, Décodage Automatique")
                                self.engine.runAndWait()
                                self.command.md.param = ""
                            case "01enter":
                                #USB
                                self.command.md.param = "004"
                                self.command.md.send(self.ser)
                                self.engine.say("OK, USB")
                                self.engine.runAndWait()
                                self.command.md.param = ""
                            case "02enter":
                                #LSB
                                self.command.md.param = "005"
                                self.command.md.send(self.ser)
                                self.engine.say("OK, LSB")
                                self.engine.runAndWait()
                                self.command.md.param = ""
                            case "03enter":
                                #CW
                                self.command.md.param = "006"
                                self.command.md.send(self.ser)
                                self.engine.say("OK, CW")
                                self.engine.runAndWait()
                                self.command.md.param = ""
                            case "08enter":
                                #AM
                                self.command.md.param = "001"
                                self.command.md.send(self.ser)
                                self.engine.say("OK, A aime")
                                self.engine.runAndWait()
                                self.command.md.param = ""
                            case "09enter":
                                #DSTAR
                                self.command.md.param = "110"
                                self.command.md.send(self.ser)
                                self.engine.say("OK, D-STAR")
                                self.engine.runAndWait()
                                self.command.md.param = ""
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
