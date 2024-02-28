import tkinter as tk
import os, shutil
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import test

def new_window(window):
    window.destroy()
    test.new_image()

def choice_image(window):
    nam = ''
    try:
        f = open('config_im.ini', 'x')
    except:
        f = open('config_im.ini', 'r')
    name = fd.askopenfilename()
    f = open('config_im.ini', 'a')
    for i in reversed(name):
        if i == "/":   
            break
        nam += i 
    nam = ''.join([i for i in reversed(nam)])
    end = '.' + os.path.dirname(__file__).replace('\\','/') +"/"+ nam
    f = open('config_im.ini', 'w')
    f = open('config_im.ini', 'a')
    f.write(nam)
    try:
       shutil.copy(name, end)
    except:
        pass
    window.destroy()
    f.close()
    main_win()
    f.close()
    
def inst_image():
    try:
        f = open('config_im.ini', 'x')
        f.write('1280x800-dscf2014-2.cb9.jpg')
    except:
        f = open('config_im.ini', 'r')
    f = open('config_im.ini', 'r')
    name = f.read()
    f.close()
    return name

def main_win():
    window = tk.Tk()
    
    window.resizable(width = False, height = False)
    try:
        logo = tk.PhotoImage(file = "logo-leti-bel-rus-vertik-2017.png")
        window.iconphoto(False, logo)    
    except:
        pass
    
    window.title("")    
    window.geometry("720x360")
    # window["bg"] = "black"
    # Add image file 
    
    
    # if config == None or config == '':
    try:
        bg = Image.open(inst_image()).resize((720, 360))
        bg = ImageTk.PhotoImage(bg)
        canvas1 = tk.Canvas(window, width = 720, height = 360) 
        canvas1.pack(fill = "both", expand = True) 
        canvas1.create_image( 0, 0, image = bg, anchor = "nw")
    except:
        bg = "green"
        canvas1 = tk.Canvas(window, width = 720, height = 360, bg = bg) 
        canvas1.pack(fill = "both", expand = True) 

    
    # name_project = tk.Label(window, text = "Навигация по проекту ", font = ("Arial Bold", 15), fg = "white", bg = "black")
    canvas1.create_text( 360, 50, text = "Навигация по проекту", font = ("Purisa", 20))
    # name_project.place(x = 220, y = 210)
    
    start_bt = tk.Button(window, text = "Начало работы",command = lambda: new_window(window), width = '40', height = "2", fg = "black", bg = "white")
    start_bt.place(x = 220, y = 110)
    
    start_bt = tk.Button(window, text = "Смена картинки",command = lambda: choice_image(window),  fg = "black", bg = "white", font='Arial 10')
    start_bt.place(x = 20, y = 300)
    
    # start_bt = tk.Button(window, text = "Начало работы",command = new_window, width = '10', height = "2", fg = "black", bg = "white")
    # start_bt.place(x = 320, y = 15)
    
    window.mainloop()
if "__main__" == __name__:
    main_win()