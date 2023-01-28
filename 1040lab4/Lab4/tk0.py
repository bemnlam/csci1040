from Tkinter import *
root = Tk()
root.title("Hello example")
root.geometry("400x300")

def sayHello():
    print 'Hello'

def sayGoodBye():
    print 'GoodBye'

Hellob = Button(root, text='Hello', command=sayHello)
newb = Button(root, text='Goodbye', command=sayGoodBye)
ent = Entry(root)
ent.pack()
ent.delete(0, END)
ent.insert(0, "a default value")
Hellob.pack()
newb.pack()
root.mainloop()
