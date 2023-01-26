# List of Commands into a class
from dv1 import Command

class Commands:
    def __init__():
        #whole command list here!
        rf = Command("RF", "", "Fréquence", {"20": "Success", "30": "Invalid frequency", "40": "Command format error", "50": "Parameter out of range"})
        zp = Command("ZP", "", "Allumage")
        qp = Command("QP", "", "Eteindre") #result code 10?
        ag = Command("AG", "", "Audio Gain")
        st = Command("ST", "", "Freq step", {"20": "Success", "30": "Invalid setting", "40": "Command format error", "50": "Parameter out of range"})
        sh = Command("SH", "", "Freq step adjust", {"20": "Success", "30": "Invalid setting", "40": "Command format error", "50": "Parameter out of range"})
        md = Command("MD", "", "Mode")
        zj = Command("ZJ", "", "Précédent")
        zk = Command("ZK", "", "Suivant")
        ex = Command("EX", "", "Stopper le remote control")
        sq = Command("SQ", "", "Sélection du squelch")
        nq = Command("NQ", "", "Valeur du Noise squelch")
        lq = Command("LQ", "", "Valeur du Level squelch")
        vq = Command("VQ", "", "Voice squelch")
        ci = Command("CI", "", "Activer le CTCSS")
        cn = Command("CN", "", "Selection du ton")
        di = Command("DI", "", "DCS ON/OFF")
        ds = Command("DS", "", "Code DCS")
        dc = Command("DC", "", "Digital CR code")
        dj = Command("DJ", "", "Sortie DATA")
        dk = Command("DK", "", "Charger le dernier message")
        ac = Command("AC", "", "AGC")
        rg = Command("RG", "", "Gain manuel")
        ifn = Command("IF", "", "Bande passante IF", {"20": "Success", "30": "Invalid decode mode", "40": "Command format error", "50": "Parameter out of range"})
        ls = Command("LS", "", "Auto Notch")
        nr = Command("NR", "", "Noise Reduction")
        of = Command("OF", "", "Offset RX")
        ol = Command("OL", "", "Offset freq", {"20": "Success", "30": "Invalid offset frequency", "40": "Command format error", "50": "Parameter out of range"})
        ox = Command("OX", "", "Monitor Offset")


