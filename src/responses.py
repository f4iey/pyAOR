# Custom response list
import serial
import pyttsx3

def lookup(res, engine):
    # Exception for frequency tts
    if res[2:4] == "RF":
        f = (res[4:12].replace('.',',') + '.' + res[12:len(res)-3]).lstrip('0')
        unit = "mégahertz"
        if len(f) == 7:
            unit = "kilohertz"
        engine.say(f.lstrip(',').rstrip('0').rstrip('.') + ' ' + unit)
        print(f.lstrip(',').rstrip('0').rstrip('.') + ' ' + unit)
        engine.runAndWait()
        return True
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
        return True
    return False
