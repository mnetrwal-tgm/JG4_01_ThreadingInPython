import threading
import random
class encrypter(threading.Thread):
    def __init__(self,msg,enDe,key):
        """
        Just initializes the Thread with the values.

        :param msg: The message
        :param enDe: Encrypt or Decrypt
        :param key: The Encryption key
        """
        #Initializing
        threading.Thread.__init__(self)
        self.msg=msg
        self.enDe=enDe
        self.key=key



    def run(self):
        """
        The encrypter/decrypter.

        :return: the en/decrypted Message
        """
        #The index
        i = 0
        #the final message
        msgnew = ""
        #The two tables for the en/decryption
        table = {' ': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
                 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22,
                 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33,
                 'y': 34, 'z': 35, 'ä': 36, 'ö': 37, 'ü': 38, 'ß': 39, 'A': 40, 'B': 41, 'C': 42, 'D': 43, 'E': 44,
                 'F': 45, 'G': 46, 'H': 47, 'I': 48, 'J': 49, 'K': 50, 'L': 51, 'M': 52, 'N': 53, 'O': 54, 'P': 55,
                 'Q': 56, 'R': 57, 'S': 58, 'T': 59, 'U': 60, 'V': 61, 'W': 62, 'X': 63, 'Y': 64, 'Z': 65, 'Ä': 66,
                 'Ö': 68, 'Ü': 69, '/': 70, ',': 71, '|': 72, }
        table2 = {0: ' ', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                  12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm',
                  23: 'n', 24: 'o', 25: 'p', 26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x',
                  34: 'y', 35: 'z', 36: 'ä', 37: 'ö', 38: 'ü', 39: 'ß', 40: 'A', 41: 'B', 42: 'C', 43: 'D', 44: 'E',
                  45: 'F', 46: 'G', 47: 'H', 48: 'I', 49: 'J', 50: 'K', 51: 'L', 52: 'M', 53: 'N', 54: 'O', 55: 'P',
                  56: 'Q', 57: 'R', 58: 'S', 59: 'T', 60: 'U', 61: 'V', 62: 'W', 63: 'X', 64: 'Y', 65: 'Z', 66: 'Ä',
                  68: 'Ö', 69: 'Ü', 70: '/', 71: ',', 72: '|'}


        if self.enDe:

            while i < len(self.msg):
                try:
                    #The character on index i gets read -> turned into int and combined with the offset -> turned into character -> added to the
                    # final string
                    msgnew+=table2[(self.key+table[self.msg[i]])%73]

                except:
                    #If the character isn't encryptable
                    print("Zeichen '"+msg[i]+"' nicht verschlüsselbar -> wird übersprungen")
                    msgnew += msg[i]

                i+=1
        else:
            while i < len(self.msg):
                try:
                    #See above, it works the exactly same way
                    msgnew += table2[(-self.key + table[self.msg[i]]) % 73]
                except:
                    print("Zeichen '"+msg[i]+"' nicht entschlüsselbar -> wird übersprungen")
                    msgnew += msg[i]
                i += 1

        return msgnew

def toIntChecker(out):
    """
    A simple method to check a User Inputs type as an integer

    :param out: what the user shall see
    :return: the User Input as an Integer
    """
    running2 = True
    while running2:
        try:
            #Takes input and trys to turn it into an integer. If it doesn't work, an error gets printed and the code
            # gets redone
            re = input(out)
            re = int(re)
            running2 = False
        except:
            print("Bitte geben sie eine Zahl ein!")

    return re










running=True
while running:
    #this is the mainscript for running the threads.
    running2=True
    usrin=toIntChecker("Wollen sie encoden [2], decoden [1] oder das programm beenden [0]?")


    if usrin <= 2 and usrin >= 1:#unfancy check if the User wants to en/decrypt
        # returns the message to encrypt and the number of threads
        msg=input("Was ist ihre Nachricht?")
        while msg=="":
            msg = input("Was ist ihre Nachricht?")
        noT=toIntChecker("Wie viele Threads wollen sie benutzen? (Maximal 1 pro Zeichen)")
        while noT > len(msg) or noT < 0:
            noT= input("Das wird nicht funktionieren. Wie viele Threads wollen sie benutzen? (Maximal 1 pro Zeichen)")

        #Generates the key or gets the key from user input
        if usrin==1:
            key = toIntChecker("Geben sie ihren decoding Key ein.")
        else:
            key = random.randrange(0,700)
            key= int(key)

        #initializes the thread list and the index-counter
        encoders = []
        i=0
        #generates the message length per thread and turns it into an integer if it is a float. the +1 guarantees the
        #full message to get encrypted
        t1=(len(msg)/noT)
        if t1%1!=0:
            t1=int(t1)+1

        #generates threads according to the before set variables.
        while i < noT:
            temp1=i*t1
            temp2=(i+1)*t1
            temp1=int(temp1)
            temp2=int(temp2)
            encoders.append(encrypter(msg[temp1:temp2],usrin-1,key))
            i+=1

        #Generates the last thread with the last characters of the thread
        temp1 = i * t1
        temp2 = i * t1 + len(msg)%noT
        temp1 = int(temp1)
        temp2 = int(temp2)
        encoders.append(encrypter(msg[temp1:temp2],usrin-1,key))

        #starts the threads and collects their data. As they finish, the encrypted/decrypted message gets printed.
        finalmsg=""
        i=0
        while i < noT :
            encoders[i].start()
            finalmsg+=encoders[i].run()
            i+=1
        i=0
        while i < noT - 1:
            encoders[i].join()
            i+=1
        print(finalmsg)

    elif usrin==0:
        #Exiting code
        print("Bye!")
        running=False
    else:
        print("Invalid Input!")
