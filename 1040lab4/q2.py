from Tkinter import *

root = Tk()
root.title("Temperature Conversion")
root.geometry("300x85")

ent = Entry(root)
ent.pack()
ent.delete(0,END)
ent.insert(0,'0')


def f2c(ent):
	f = float(ent.get())
	ans = (5.0/9.0)*(f-32.0)
	print ans
	ent.delete(0,END)
	ent.insert(0,str(ans))

def c2f(ent):
	c = float(ent.get())
	ans = c*9.0/5.0 + 32.0
	print ans
	ent.delete(0,END)
	ent.insert(0,str(ans))

cb = Button(root, text='Celsius',	 command = lambda: f2c(ent) )
cf = Button(root, text='Fahrenheit', command = lambda: c2f(ent) )

cb.pack()
cf.pack()

root.mainloop()

