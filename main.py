import serial
import pyttsx3
from Commands import *

# Initialisation de la synthèse vocale en francais
engine = pyttsx3.init()
engine.setProperty('voice', 'fr')

# Ouverture du port série
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)

# Première commande pour afficher la fréquence
Commands = Commands()
Commands.rf.send(ser)
print(Commands.rf.response(ser, engine))

# Fermeture du port série
ser.close()

