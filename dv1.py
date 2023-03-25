# List of functions to control AOR AR-DV1
import serial
class Command:
    def __init__(self, name, parameter, desc):
        self.name = name
        self.param = parameter
        self.desc = desc
        self.result_code = {"20": "Success", "30": "Not executable", "40": "Command format error", "50": "Parameter out of range", "60": "Unkown command"}
       # self.engine = pyttsx3.init()

    def send(self, ser):
        ser.write((self.name + self.param + "\r").encode('ascii', 'ignore'))

    def response(self, ser):
        res = ser.readline().decode()
        for k in self.result_code.keys():
            if res[0:2] == k and k != "20":
                print(self.result_code[k])
                return
        if len(res) <= 5:
            print(self.desc + " : " + self.param)
            return
        print(self.desc + " : " + res[4:])
        return res [4:]
