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
            engine.say(self.desc + " : " + f.lstrip(',').rstrip('0').rstrip('.').rstrip('0') + ' ' + unit)
            engine.runAndWait()
            return
        if len(res) <= 5:
            engine.say(self.desc + " : " + self.param)
            engine.runAndWait()
            return
        engine.say(self.desc + " : " + res[4:])
        engine.runAndWait()
        return res [4:]
