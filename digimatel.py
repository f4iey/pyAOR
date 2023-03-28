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
        keyboard.add_hotkey("dot", self.get_freq)
        keyboard.add_hotkey("6", self.other_hotkey)
        keyboard.add_hotkey("4", self.other_hotkey)

        keyboard.wait()  # Attends jusqu'à ce que l'utilisateur appuie sur une touche pour arrêter le programme
        keyboard.unhook_all()  # Libère les raccourcis clavier
    def get_freq(self):
        self.command.rf.send(self.ser)
        return self.command.rf.response(self.ser, self.engine)
    def other_hotkey(self):
        pass
