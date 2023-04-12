from tkinter import *
import tkinter as tk


def bh():
    master = tk.Tk()
    bgimg= tk.PhotoImage(file = "color_bars.png")
    #Specify the file name present in the same directory or else
    #specify the proper path for retrieving the image to set it as background image.
    limg= Label(master, i=bgimg)
    limg.pack()
    return master.mainloop()

bh()