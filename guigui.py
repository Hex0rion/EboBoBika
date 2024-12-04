#!/usr/local/bin/python
# coding: latin-1
from tkinter import *
# import ttk
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("AIS")
root.configure(bg="#ECECEC")
root.resizable(0, 0)

#-----------------------------------------------------Styles------------------------------------------------------------

frameStyle = ttk.Style()
frameStyle.theme_use('vista')

comboboxStyle = ttk.Style()
comboboxStyle.theme_use('vista')

#-----------------------------------------------------------------------------------------------------------------------

frameGlobal = Frame(root, width=800, height=600, bg="#ECECEC")
frameGlobal.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------

labelFrameGlobal1 = LabelFrame(frameGlobal, text="Function", bg="#ECECEC")
labelFrameGlobal1.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------

imageBoxFunc = ImageTk.PhotoImage(Image.open("none.gif"))
labelImgBoxFunc = ttk.Label(labelFrameGlobal1, image=imageBoxFunc, borderwidth="2px", relief="ridge")
labelImgBoxFunc.grid(column=0, row=1, padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------
def boxFunctions_select(*args):
    elem = boxFunctionsVar.get()
    if elem == "":
        newimg = ImageTk.PhotoImage(Image.open("none.gif"))
        labelImgBoxFunc.configure(image=newimg)
        labelImgBoxFunc.image = newimg
    if elem == "IC function":
        newimg = ImageTk.PhotoImage(Image.open("icfunc.gif"))
        labelImgBoxFunc.configure(image=newimg)
        labelImgBoxFunc.image = newimg

boxFunctionsValues = ["", "IC function"]
boxFunctionsVar = StringVar()
boxFunctions = ttk.Combobox(labelFrameGlobal1, textvariable=boxFunctionsVar, values=boxFunctionsValues, state="readonly")
boxFunctions.grid(column=0, row=0)
boxFunctions.bind('<<ComboboxSelected>>', boxFunctions_select)

#-----------------------------------------------------------------------------------------------------------------------

frameTableGoodX = Frame(labelFrameGlobal1, bg="white", borderwidth="2px", relief="ridge")
frameTableGoodX.grid(column=0, row=2, sticky=(N, W, E, S), padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------

Label(frameTableGoodX, text = "", bg="white", width=5).grid(column=0, row=0, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=1, row=0, sticky=(N, W, E, S))
Label(frameTableGoodX, text = "a", bg="white", width=5).grid(column=2, row=0, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=3, row=0, sticky=(N, W, E, S))
Label(frameTableGoodX, text = "b", bg="white", width=5).grid(column=4, row=0, sticky=(N, W, E, S))

ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=0, row=1, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=1, row=1, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=2, row=1, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=3, row=1, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=4, row=1, sticky=(N, W, E, S))

Label(frameTableGoodX, text = "x1", bg="white", width=5).grid(column=0, row=2, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=1, row=2, sticky=(N, W, E, S))

x1A = StringVar()
x1B = StringVar()

entryX1A = Entry(frameTableGoodX, textvariable=x1A, width=5)
entryX1A.grid(column=2, row=2, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=3, row=2, sticky=(N, W, E, S))
entryX1B = Entry(frameTableGoodX, textvariable=x1B, width=5)
entryX1B.grid(column=4, row=2, sticky=(N, W, E, S))


ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=0, row=3, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=1, row=3, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=2, row=3, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=3, row=3, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=4, row=3, sticky=(N, W, E, S))

Label(frameTableGoodX, text = "x2", bg="white", width=5).grid(column=0, row=4, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=1, row=4, sticky=(N, W, E, S))

x2A = StringVar()
x2B = StringVar()

entryX2A = Entry(frameTableGoodX, textvariable=x2A, width=5)
entryX2A.grid(column=2, row=4, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=3, row=4, sticky=(N, W, E, S))
entryX2B = Entry(frameTableGoodX, textvariable=x2B, width=5)
entryX2B.grid(column=4, row=4, sticky=(N, W, E, S))

ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=0, row=5, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=1, row=5, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=2, row=5, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=3, row=5, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=4, row=5, sticky=(N, W, E, S))

Label(frameTableGoodX, text = "x3", bg="white", width=5).grid(column=0, row=6, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=1, row=6, sticky=(N, W, E, S))

x3A = StringVar()
x3B = StringVar()

entryX3A = Entry(frameTableGoodX, textvariable=x3A, width=5)
entryX3A.grid(column=2, row=6, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=3, row=6, sticky=(N, W, E, S))
entryX3B = Entry(frameTableGoodX, textvariable=x3B, width=5)
entryX3B.grid(column=4, row=6, sticky=(N, W, E, S))

#ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=0, row=7, sticky=(N, W, E, S))
#ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=1, row=7, sticky=(N, W, E, S))
#ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=2, row=7, sticky=(N, W, E, S))
#ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=3, row=7, sticky=(N, W, E, S))
#ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=4, row=7, sticky=(N, W, E, S))


#-----------------------------------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------------------------------


mainloop()