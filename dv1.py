# List of functions to control AOR AR-DV1
import serial
import pyttsx3

class Command:
    def __init__(self, name, parameter, desc):
        self.name = name
        self.param = parameter
        self.desc = desc
        self.result_code = {"20": "Success", "30": "Not executable", "40": "Command format error", "50": "Parameter out of range", "60": "Unkown command"}
       # self.engine = pyttsx3.init()

    def send(self, ser):
        ser.write((self.name + self.param + "\r").encode('ascii', 'ignore'))

    def response(self, ser, engine):
        res = ser.readline().decode()
        for k in self.result_code.keys():
            if res[0:2] == k and k != "20":
                print(self.result_code[k])
                return
        # Exception for frequency tts
        if res[2:4] == "RF":
            f = (res[4:12].replace('.',',') + '.' + res[12:len(res)-3]).lstrip('0')
            unit = "mégahertz"
            if len(f) == 7:
                unit = "kilohertz"
            engine.say(f.lstrip(',').rstrip('0').rstrip('.').rstrip('0') + ' ' + unit)
            print(f.lstrip(',').rstrip('0').rstrip('.').rstrip('0') + ' ' + unit)
            engine.runAndWait()
            return res [4:]
        elif res[2:4] == "MD":
            m = res[4:]
            if m[0] != "0" or m[1] != "F":
                engine.say("Numérique")
                engine.runAndWait()
                match(m[1]):
                    case "0":
                        engine.say("Décodage automatique")
                    case "1":
                        engine.say("D-STAR")
                    case "2":
                        engine.say("Fusion")
                    case "3":
                        engine.say("Alinco")
                    case "5":
                        engine.say("P25")
                    case "6":
                        engine.say("dPMR")
                    case "7":
                        engine.say("DMR")
                engine.runAndWait()
            else:
                match(m[2]):
                    case "0":
                        engine.say("FM")
                    case "1":
                        engine.say("AM")
                    case "2":
                        engine.say("SAH")
                    case "3":
                        engine.say("SAL")
                    case "4":
                        engine.say("USB")
                    case "5":
                        engine.say("LSB")
                    case "6":
                        engine.say("CW")
                engine.runAndWait()
            return res [4:]
        if len(res) <= 5:
            engine.say(self.desc + " : " + self.param)
            engine.runAndWait()
            return res [4:]
        engine.say(self.desc + " : " + res[4:])
        engine.runAndWait()
        return res [4:]
