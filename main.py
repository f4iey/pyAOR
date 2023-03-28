import serial
import time
import pyttsx3
from Commands import *

# Initialisation de la synthèse vocale en francais
engine = pyttsx3.init()
engine.setProperty('voice', 'french+f4')
engine.setProperty('rate', 150)

# Ouverture du port série
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)

# Première commande d'exemple qui reboot et prononce la freq
Commands = Commands()
#Commands.qp.send(ser)
#print(Commands.qp.response(ser, engine))
#time.sleep(3)
#Commands.zp.send(ser)
#print(Commands.zp.response(ser, engine))
#time.sleep(4)
#ser.close()
# On rouvre le session pour lire la freq de nouveau
#ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)
Commands.rf.send(ser)
print(Commands.rf.response(ser, engine))

# Fermeture du port série
ser.close()

