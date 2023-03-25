import serial
from Commands import *

# Ouverture du port série
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)

# Première commande pour afficher la fréquence
Commands = Commands()
rf.send(ser)
rf.response(ser)

# Fermeture du port série
ser.close()

