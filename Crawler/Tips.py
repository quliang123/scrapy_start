# coding=utf-8
import Tkinter
import time

top = Tkinter.Tk()

time.sleep(1800)
lable = Tkinter.Label(top, text="30分钟到了")

lable.pack()
top.mainloop()
