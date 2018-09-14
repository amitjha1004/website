# from Tkinter import *
# from Tkinter
#
# root = Tk()
# root.title('FirstGUI')
# w = Label(root, text="Hello World")
# Tkinter.Button(root, text="Button").grid()
# w.pack()
# root.mainloop()


import Tkinter
import tkMessageBox


top = Tkinter.Tk()


def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")


B = Tkinter.Button(top, text ="Hello", command = helloCallBack)

B.pack()
top.mainloop()

sentence = "India is great"
words = sentence.split()
sentence_rev = " ".join(reversed(words))
print sentence_rev

d = {1:2,2:3}
# print d.get(1)
print d.keys()

# import re
# a = "123abc"
# t = re.match("[a-z]+",a)
# t = re.search("[a-z]+",a)
#
#
# classA:
# 	deffun(self,a,b):
# 	    return a+b
# 	deffun(self):
# 	    return a+b
#
# 	obj = A()
# 	print(obj.fun(1,2))

'TURBO'[::-1]