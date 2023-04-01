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
        keyboard.add_hotkey("num enter", self.get_freq_mode)
        keyboard.add_hotkey("numlock", self.numlock)
        keyboard.add_hotkey("num minus", self.minus)
        keyboard.add_hotkey("6", self.other_hotkey)
        keyboard.add_hotkey("4", self.other_hotkey)

        keyboard.wait()  # Attends jusqu'à ce que l'utilisateur appuie sur une touche pour arrêter le programme
        keyboard.unhook_all()  # Libère les raccourcis clavier
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
    def other_hotkey(self):
        pass
