#!/usr/local/bin/python
# coding: utf-8
from tkinter import *
# import ttk
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("AIS")
root.configure(bg="#ECECEC", width=800, height=600)
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

Label(frameGlobal, text="Вид целевой функции", bg="#ECECEC", font="Helvetica 14 bold").grid(column=0, row=0, sticky=(N, W, E, S))

#-----------------------------------------------------------------------------------------------------------------------

frameImgBoxFunc = Frame(frameGlobal, bg="white", borderwidth="2px", relief="ridge")
frameImgBoxFunc.grid(column=0, row=2, padx=19, sticky=(N, W, E, S))

imageBoxFunc = ImageTk.PhotoImage(Image.open("none.gif"))
labelImgBoxFunc = ttk.Label(frameImgBoxFunc, image=imageBoxFunc)#, borderwidth="2px", relief="ridge")
labelImgBoxFunc.grid(column=0, row=0)

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
boxFunctions = ttk.Combobox(frameGlobal, textvariable=boxFunctionsVar, values=boxFunctionsValues, state="readonly")
boxFunctions.grid(column=0, row=1)
boxFunctions.bind('<<ComboboxSelected>>', boxFunctions_select)

#-----------------------------------------------------------------------------------------------------------------------

frameTableGoodX = Frame(frameGlobal, bg="white", borderwidth="2px", relief="ridge")
frameTableGoodX.grid(column=0, row=3, sticky=(N, W, E, S), padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------

Label(frameTableGoodX, text = "", bg="white", width=10).grid(column=0, row=0, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=1, row=0, sticky=(N, W, E, S))
Label(frameTableGoodX, text = "a", bg="white", width=10, font="Helvetica 14 bold").grid(column=2, row=0, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=3, row=0, sticky=(N, W, E, S))
Label(frameTableGoodX, text = "b", bg="white", width=10, font="Helvetica 14 bold").grid(column=4, row=0, sticky=(N, W, E, S))

ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=0, row=1, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=1, row=1, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=2, row=1, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=3, row=1, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=4, row=1, sticky=(N, W, E, S))

Label(frameTableGoodX, text = "x1", bg="white", width=10, font="Helvetica 14 bold").grid(column=0, row=2, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=1, row=2, sticky=(N, W, E, S))

x1A = StringVar()
x1B = StringVar()

entryX1A = Entry(frameTableGoodX, textvariable=x1A, width=10)
entryX1A.grid(column=2, row=2, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=3, row=2, sticky=(N, W, E, S))
entryX1B = Entry(frameTableGoodX, textvariable=x1B, width=10)
entryX1B.grid(column=4, row=2, sticky=(N, W, E, S))


ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=0, row=3, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=1, row=3, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=2, row=3, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=3, row=3, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=4, row=3, sticky=(N, W, E, S))

Label(frameTableGoodX, text = "x2", bg="white", width=10, font="Helvetica 14 bold").grid(column=0, row=4, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=1, row=4, sticky=(N, W, E, S))

x2A = StringVar()
x2B = StringVar()

entryX2A = Entry(frameTableGoodX, textvariable=x2A, width=10)
entryX2A.grid(column=2, row=4, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=3, row=4, sticky=(N, W, E, S))
entryX2B = Entry(frameTableGoodX, textvariable=x2B, width=10)
entryX2B.grid(column=4, row=4, sticky=(N, W, E, S))

ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=0, row=5, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=1, row=5, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=2, row=5, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=3, row=5, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=4, row=5, sticky=(N, W, E, S))

Label(frameTableGoodX, text = "x3", bg="white", width=10, font="Helvetica 14 bold").grid(column=0, row=6, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=1, row=6, sticky=(N, W, E, S))

x3A = StringVar()
x3B = StringVar()

entryX3A = Entry(frameTableGoodX, textvariable=x3A, width=10)
entryX3A.grid(column=2, row=6, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=VERTICAL).grid(column=3, row=6, sticky=(N, W, E, S))
entryX3B = Entry(frameTableGoodX, textvariable=x3B, width=10)
entryX3B.grid(column=4, row=6, sticky=(N, W, E, S))

ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=0, row=7, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=1, row=7, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=2, row=7, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=3, row=7, sticky=(N, W, E, S))
ttk.Separator(frameTableGoodX, orient=HORIZONTAL).grid(column=4, row=7, sticky=(N, W, E, S))


#-----------------------------------------------------------------------------------------------------------------------

Label(frameGlobal, text="Параметры функции", bg="#ECECEC", font="Helvetica 14 bold").grid(column=1, row=0, padx=20, sticky=(N, W, E, S))

#-----------------------------------------------------------------------------------------------------------------------

frameParametrsFunc = Frame(frameGlobal, bg="white", borderwidth="2px", relief="ridge")
frameParametrsFunc.grid(column=1, row=2, padx=20, sticky=(N, W, E, S))

#-----------------------------------------------------------------------------------------------------------------------

Label(frameParametrsFunc, text = "Параметр", bg="white", width=20, font="Helvetica 14 bold").grid(column=0, row=0, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=0, sticky=(N, W, E, S))
Label(frameParametrsFunc, text = "Значение", bg="white", width=10, font="Helvetica 14 bold").grid(column=2, row=0, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=1, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=1, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=1, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "Деньги, D", bg="white", width=10).grid(column=0, row=2, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=2, sticky=(N, W, E, S))

D = StringVar()
entryD = Entry(frameParametrsFunc, textvariable=D, width=10)
entryD.grid(column=2, row=2, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=3, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=3, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=3, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "Текущий год, n", bg="white", width=10).grid(column=0, row=4, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=4, sticky=(N, W, E, S))

n = StringVar()
entryn = Entry(frameParametrsFunc, textvariable=n, width=10)
entryn.grid(column=2, row=4, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=5, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=5, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=5, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "С1", bg="white", width=10).grid(column=0, row=6, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=6, sticky=(N, W, E, S))

C1 = StringVar()
entryn = Entry(frameParametrsFunc, textvariable=C1, width=10)
entryn.grid(column=2, row=6, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=7, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=7, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=7, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "С2", bg="white", width=10).grid(column=0, row=8, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=8, sticky=(N, W, E, S))

C2 = StringVar()
entryn = Entry(frameParametrsFunc, textvariable=C2, width=10)
entryn.grid(column=2, row=8, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=9, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=9, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=9, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "С3", bg="white", width=10).grid(column=0, row=10, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=10, sticky=(N, W, E, S))

C3 = StringVar()
entryn = Entry(frameParametrsFunc, textvariable=C3, width=10)
entryn.grid(column=2, row=10, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=11, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=11, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=11, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "С4", bg="white", width=10).grid(column=0, row=12, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=12, sticky=(N, W, E, S))

C4 = StringVar()
entryn = Entry(frameParametrsFunc, textvariable=C4, width=10)
entryn.grid(column=2, row=12, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=13, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=13, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=13, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "С5", bg="white", width=10).grid(column=0, row=14, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=14, sticky=(N, W, E, S))

C5 = StringVar()
entryn = Entry(frameParametrsFunc, textvariable=C5, width=10)
entryn.grid(column=2, row=14, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=15, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=15, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=15, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "С6", bg="white", width=10).grid(column=0, row=16, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=16, sticky=(N, W, E, S))

C6 = StringVar()
entryn = Entry(frameParametrsFunc, textvariable=C6, width=10)
entryn.grid(column=2, row=16, sticky=(N, W, E, S))

ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=0, row=17, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=1, row=17, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=HORIZONTAL).grid(column=2, row=17, sticky=(N, W, E, S))

Label(frameParametrsFunc, text = "С7", bg="white", width=10).grid(column=0, row=18, sticky=(N, W, E, S))
ttk.Separator(frameParametrsFunc, orient=VERTICAL).grid(column=1, row=18, sticky=(N, W, E, S))

C7 = StringVar()
entryn = Entry(frameParametrsFunc, textvariable=C7, width=10)
entryn.grid(column=2, row=18, sticky=(N, W, E, S))

#-----------------------------------------------------------------------------------------------------------------------

frameRestrictions = Frame(frameGlobal, bg="white", borderwidth="2px", relief="ridge")
frameRestrictions.grid(column=1, row=3, sticky=(N, W, E, S), padx=10, pady=10)

#-----------------------------------------------------------------------------------------------------------------------

Label(frameRestrictions, text = "Ограничения", bg="white", font="Helvetica 14 bold").grid(column=0, row=0, padx=3, pady=20)

#buttonPlusRestriction = Button(frameRestrictions, text="+", bg="#ECECEC")
#buttonPlusRestriction.grid(column=1, row=0, padx=3, pady=3)

restrinctions = StringVar()
entryRestrictions = Entry(frameRestrictions, bg="white", textvariable=restrinctions, width=30)
entryRestrictions.grid(column=0, row=1, padx=13)

#-----------------------------------------------------------------------------------------------------------------------

Label(frameGlobal, text="Параметры алгоритма", bg="#ECECEC", font="Helvetica 14 bold").grid(column=2, row=0, padx=45, sticky=(N, W, E, S))

frameParametrsAlg = Frame(frameGlobal, bg="#ECECEC")#, borderwidth="2px", relief="ridge")
frameParametrsAlg.grid(column=2, row=2, padx=20, sticky=(N, W, E, S))

frameParametrsAlg1 = Frame(frameParametrsAlg, bg="white", borderwidth="2px", relief="ridge")
frameParametrsAlg1.grid(column=0, row=2, sticky=(N, W, E, S))

#-----------------------------------------------------------------------------------------------------------------------

Label(frameParametrsAlg1, text = "Параметр", bg="white", width=20, font="Helvetica 14 bold").grid(column=0, row=3, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=VERTICAL).grid(column=1, row=3, sticky=(N, W, E, S))
Label(frameParametrsAlg1, text = "Значение", bg="white", font="Helvetica 14 bold", width=10).grid(column=2, row=3, sticky=(N, W, E, S))

ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=0, row=4, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=1, row=4, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=2, row=4, sticky=(N, W, E, S))

Label(frameParametrsAlg1, text = "Ip", bg="white", width=20).grid(column=0, row=5, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=VERTICAL).grid(column=1, row=5, sticky=(N, W, E, S))

strIp = StringVar()
entryn = Entry(frameParametrsAlg1, textvariable=strIp, width=10)
entryn.grid(column=2, row=5, sticky=(N, W, E, S))

ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=0, row=6, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=1, row=6, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=2, row=6, sticky=(N, W, E, S))

Label(frameParametrsAlg1, text = "sigma", bg="white", width=20).grid(column=0, row=7, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=VERTICAL).grid(column=1, row=7, sticky=(N, W, E, S))

strSigma = StringVar()
entryn = Entry(frameParametrsAlg1, textvariable=strSigma, width=10)
entryn.grid(column=2, row=7, sticky=(N, W, E, S))

ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=0, row=8, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=1, row=8, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=2, row=8, sticky=(N, W, E, S))

Label(frameParametrsAlg1, text = "d", bg="white", width=20).grid(column=0, row=9, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=VERTICAL).grid(column=1, row=9, sticky=(N, W, E, S))

strd = StringVar()
entryn = Entry(frameParametrsAlg1, textvariable=strd, width=10)
entryn.grid(column=2, row=9, sticky=(N, W, E, S))

ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=0, row=10, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=1, row=10, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=2, row=10, sticky=(N, W, E, S))

Label(frameParametrsAlg1, text = "K", bg="white", width=20).grid(column=0, row=11, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=VERTICAL).grid(column=1, row=11, sticky=(N, W, E, S))

strK = StringVar()
entryn = Entry(frameParametrsAlg1, textvariable=strK, width=10)
entryn.grid(column=2, row=11, sticky=(N, W, E, S))

ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=0, row=12, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=1, row=12, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=2, row=12, sticky=(N, W, E, S))

Label(frameParametrsAlg1, text = "epsilon", bg="white", width=20).grid(column=0, row=13, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=VERTICAL).grid(column=1, row=13, sticky=(N, W, E, S))

strEpsilon = StringVar()
entryn = Entry(frameParametrsAlg1, textvariable=strEpsilon, width=10)
entryn.grid(column=2, row=13, sticky=(N, W, E, S))

ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=0, row=14, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=1, row=14, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=2, row=14, sticky=(N, W, E, S))

Label(frameParametrsAlg1, text = "Nc", bg="white", width=20).grid(column=0, row=15, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=VERTICAL).grid(column=1, row=15, sticky=(N, W, E, S))

strNc = StringVar()
entryn = Entry(frameParametrsAlg1, textvariable=strNc, width=10)
entryn.grid(column=2, row=15, sticky=(N, W, E, S))

ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=0, row=16, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=1, row=16, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=HORIZONTAL).grid(column=2, row=16, sticky=(N, W, E, S))

Label(frameParametrsAlg1, text = "gamma", bg="white", width=20).grid(column=0, row=17, sticky=(N, W, E, S))
ttk.Separator(frameParametrsAlg1, orient=VERTICAL).grid(column=1, row=17, sticky=(N, W, E, S))

strGamma = StringVar()
entryn = Entry(frameParametrsAlg1, textvariable=strGamma, width=10)
entryn.grid(column=2, row=17, sticky=(N, W, E, S))

#-----------------------------------------------------------------------------------------------------------------------

frameResults = Frame(frameGlobal, bg="#ECECEC")
frameResults.grid(column=2, row=3, sticky=(N, W, E, S), padx=20, pady=10)

#-----------------------------------------------------------------------------------------------------------------------

Label(frameResults, text = "Результаты работы алгоритма", bg="#ECECEC", font="Helvetica 14 bold").grid(column=0, row=0, padx=10)

frameResults1 = Frame(frameResults, bg="white", borderwidth="2px", relief="ridge")
frameResults1.grid(column=0, row=1, sticky=(N, W, E, S))

Label(frameResults1, text = "Параметр", bg="white", width=20, font="Helvetica 14 bold").grid(column=0, row=2, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=VERTICAL).grid(column=1, row=2, sticky=(N, W, E, S))
Label(frameResults1, text = "Значение", bg="white", font="Helvetica 14 bold", width=10).grid(column=2, row=2, sticky=(N, W, E, S))

ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=0, row=3, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=1, row=3, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=2, row=3, sticky=(N, W, E, S))

Label(frameResults1, text = "x1", bg="white", width=20).grid(column=0, row=4, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=VERTICAL).grid(column=1, row=4, sticky=(N, W, E, S))

labelResX1 = Label(frameResults1, text = "", bg="white").grid(column=2, row=4, sticky=(N, W, E, S))

ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=0, row=5, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=1, row=5, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=2, row=5, sticky=(N, W, E, S))

Label(frameResults1, text = "x2", bg="white", width=20).grid(column=0, row=6, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=VERTICAL).grid(column=1, row=6, sticky=(N, W, E, S))

labelResX2 = Label(frameResults1, text = "", bg="white").grid(column=2, row=6, sticky=(N, W, E, S))

ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=0, row=7, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=1, row=7, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=2, row=7, sticky=(N, W, E, S))

Label(frameResults1, text = "x3", bg="white", width=20).grid(column=0, row=8, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=VERTICAL).grid(column=1, row=8, sticky=(N, W, E, S))

labelResX3 = Label(frameResults1, text = "", bg="white").grid(column=2, row=8, sticky=(N, W, E, S))

ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=0, row=9, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=1, row=9, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=HORIZONTAL).grid(column=2, row=9, sticky=(N, W, E, S))

Label(frameResults1, text = "f", bg="white", width=20).grid(column=0, row=10, sticky=(N, W, E, S))
ttk.Separator(frameResults1, orient=VERTICAL).grid(column=1, row=10, sticky=(N, W, E, S))

labelResX3 = Label(frameResults1, text = "", bg="white").grid(column=2, row=10, sticky=(N, W, E, S))

#-----------------------------------------------------------------------------------------------------------------------

Label(frameGlobal, text="График функции в трехмерном измерении", bg="#ECECEC", font="Helvetica 14 bold").grid(column=3, row=0, sticky=(N, W, E, S))

#-----------------------------------------------------------------------------------------------------------------------



mainloop()