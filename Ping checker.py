import subprocess
import Tkinter
from Tkinter import *

def pinger(x):#gets the info and returns as a string
    P = subprocess.Popen(["ping.exe",x],stdout = subprocess.PIPE)
    simplifiedP = P.communicate()[0].splitlines()
    for i in range(0,5):
        del simplifiedP[0]
    return "\n".join(simplifiedP)
    
x = "104.160.131.1"
root = Tkinter.Tk()
text = Text(root)
text.insert(INSERT,pinger(x))
text.pack()
root.mainloop()
