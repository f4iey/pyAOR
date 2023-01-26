import serial
import pyttsx3

# Initialisation de la synthèse vocale
engine = pyttsx3.init()

# Ouverture du port série
ser = serial.Serial("/dev/ttyUSB0", baudrate=115200)

# Première commande pour afficher la fréquence
rf = Command("RF", "", "Fréquence", {"20": "Success", "30": "Invalid frequency", "40": "Command format error", "50": "Parameter out of range"})
rf.send(ser)
print(rf.response(ser, engine))

# Fermeture du port série
ser.close()

