#!/usr/local/bin/python
# coding: utf-8
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
#import styles

root = Tk()
root.title("AIS")

framestyle = ttk.Style()
framestyle.theme_create('framestyle', parent="default",
                        settings = {"Input.TFrame":
                                        {"configure":
                                             {'selectbackground': 'blue',
                                                'fieldbackground': 'white',
                                                'background': 'white'
                                             }}})
framestyle.theme_use("framestyle")

mainframe = ttk.Frame(root, padding="10 10 10 10", relief="groove", style="Input.TFrame")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=10, pady=10)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

labelstyle = ttk.Style()
labelstyle.theme_create('labelstyle', parent='default',
                         settings = {'Input.TLabel':
                                     {'configure':
                                      {'selectbackground': 'blue',
                                       'fieldbackground': 'white',
                                       'background': 'white'
                                       }}})

labelstyle.configure("Input.TLabel", font=('Helvetica', 14))
labelstyle.theme_use('labelstyle')

ttk.Label(mainframe, text="Входные данные", style="Input.TLabel").grid(column=0, row=0)

mainframe_ch1 = ttk.Frame(mainframe, padding="10 10 10 10", relief="groove", style="Input.TFrame")
mainframe_ch1.grid(column=0, row=1, sticky=(N, W, E, S), padx=10, pady=10)
mainframe_ch1.columnconfigure(0, weight=1)
mainframe_ch1.rowconfigure(0, weight=1)


ttk.Label(mainframe_ch1, text="Целевая функция").grid(column=0, row=0)

img = ImageTk.PhotoImage(Image.open("none.gif"))
imglabel = ttk.Label(mainframe_ch1, image=img, borderwidth=2, relief="groove")
imglabel.grid(column=0, row=2, pady=5)

def select(*args):
    elem = combobox.get()
    if elem == "Ackley":
        newimg = ImageTk.PhotoImage(Image.open("ackley.gif"))
        imglabel.configure(image=newimg)
        imglabel.image = newimg
        newimg1 = ImageTk.PhotoImage(Image.open("ack.gif"))
        imglabel1.configure(image=newimg1)
        imglabel1.image = newimg1
        print ("Ackley")
    if elem =="Rosenbrock":
        print ("Rosenbrock")

combobox = StringVar()
combob = ttk.Combobox(mainframe_ch1, textvariable=combobox, values=["Ackley", "Rosenbrock"])
combob.grid(column=0, row=1)
combob.bind('<<ComboboxSelected>>', select)

#ttk.Label(mainframe_ch1, text="Множество допустимых значений").grid(column=0, row=4, pady=10)

#mainframe_ch1_ch1 = ttk.Frame(mainframe_ch1, padding="10 10 10 10", relief="groove", style="Input.TFrame")
#mainframe_ch1_ch1.grid(column=0, row=5, sticky=(N, W, E, S), padx=10, pady=10)
#mainframe_ch1_ch1.columnconfigure(0, weight=1)
#mainframe_ch1_ch1.rowconfigure(0, weight=1)
#ttk.Label(mainframe_ch1_ch1, text="", width=10, borderwidth=2, relief="groove").grid(column=0, row=0)
#ttk.Label(mainframe_ch1_ch1, text="a", width=10, borderwidth=2, relief="groove").grid(column=1, row=0)
#ttk.Label(mainframe_ch1_ch1, text="b", width=10, borderwidth=2, relief="groove").grid(column=2, row=0)
#ttk.Label(mainframe_ch1_ch1, text="x1", width=10, borderwidth=2, relief="groove").grid(column=0, row=1)
#ttk.Label(mainframe_ch1_ch1, text="x2", width=10, borderwidth=2, relief="groove").grid(column=0, row=2)

#x1a = StringVar()
#x1b = StringVar()
#x2a = StringVar()
#x2b = StringVar()

#var_x1a = ttk.Entry(mainframe_ch1_ch1, textvariable=x1a, width=10)
#var_x1a.grid(column=1, row=1)
#var_x1b = ttk.Entry(mainframe_ch1_ch1, textvariable=x1b, width=10)
#var_x1b.grid(column=2, row=1)
#var_x2a = ttk.Entry(mainframe_ch1_ch1, textvariable=x2a, width=10)
#var_x2a.grid(column=1, row=2)
#var_x2b = ttk.Entry(mainframe_ch1_ch1, textvariable=x2b, width=10)
#var_x2b.grid(column=2, row=2)


mainframe_ch2 = ttk.Frame(mainframe, padding="10 10 10 10", relief="groove")
mainframe_ch2.grid(column=1, row=1, sticky=(N, W, E, S))
mainframe_ch2.columnconfigure(0, weight=1)
mainframe_ch2.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Графическое представление функции", style="Input.TLabel").grid(column=1, row=0, padx=5)

img_gr = ImageTk.PhotoImage(Image.open("none1.gif"))
imglabel1 = ttk.Label(mainframe_ch2, image=img, borderwidth=2, relief="groove", width=500)
imglabel1.grid(column=0, row=1)


root.mainloop()