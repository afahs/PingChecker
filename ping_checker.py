from datetime import datetime	# timestamp
from Tkinter import *			# Python Tk bindings

try:				# try to import pyping
	from pyping import ping
except ImportError:	# install it if not, then import
	from subprocess import Popen,PIPE

	# create and execute a pip process to
	# install the pyping module
	proc=Popen(['pip2','install','pyping'],stdout=PIPE,stderr=PIPE)
	out,err=proc.communicate()

	# import the method
	from pyping import ping

# ping wrapper method
def tick():
	# call the pyping method
	delay=ping('104.160.131.1')
	# append timestamp + ping to the Tk text box
	text.insert(INSERT,"[%s] %.3fms\n"%(str(datetime.now()).split('.')[0],float(delay.avg_rtt)))

# create Tk objects
root=Tk()
text=Text(root)
Button(root,text='Ping',command=tick).pack()

# pack and initialize text
text.pack()
tick()

# start GUI
root.mainloop()