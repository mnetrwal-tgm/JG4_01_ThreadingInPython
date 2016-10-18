import threading
import math
class encrypter(threading.Thread):
    def __init__(self,msg,noT,enDe,key = math.radians(0, 700)):

        #Initializing
        threading.Thread.__init__(self)
        self.msg=msg
        self.noT=noT
        self.enDe=enDe
        self.key=key



    def run(self):

        i = 0
        msgnew = ""
        table = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
                 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23,
                 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34,
                 'z': 35, 'ä': 36, 'ö': 37, 'ü': 38, 'ß': 39, 'A': 40, 'B': 41, 'C': 42, 'D': 43, 'E': 44, 'F': 45,
                 'G': 46, 'H': 47, 'I': 48, 'J': 49, 'K': 50, 'L': 51, 'M': 52, 'N': 53, 'O': 54, 'P': 55, 'Q': 56,
                 'R': 57, 'S': 58, 'T': 59, 'U': 60, 'V': 61, 'W': 62, 'X': 63, 'Y': 64, 'Z': 65, 'Ä': 66, 'Ö': 68,
                 'Ü': 69, '/': 70, ',': 71, '|': 72, ' ': 73}

        if self.enDe:
            while i <= self.msg.length:
                msgnew+=table[(self.key+table[self.msg[i]])%72]
        else:
            while i <= self.msg.length:
                msgnew+=table[(self.key-table[self.msg[i]])%72]

        return msgnew
