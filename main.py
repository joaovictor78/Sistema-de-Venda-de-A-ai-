from tkinter import *
from PIL import Image, ImageTk
class Application:
    def __init__(self, master=None):
        master.configure(bg="white")
        master.iconbitmap ("img/icon_aba1.ico")
        master.title("Universo Açaí - Sabor com qualidade!")
        w = Canvas(master, borderwidth = 0, highlightthickness = 0)
        w.configure(bg="white")
        w.pack(expand="true")
        widget1 = Label(w, borderwidth = 0, highlightthickness = 0)
        widget1.configure(bg="white")
        widget1.pack(side=LEFT)
        image = ImageTk.PhotoImage(file="img/logo.png")
        label = Label(widget1, image=image, bg="white")
        master.image = image
        label.pack()
        title = Label(widget1, fg="#642B8A", bg="white")
        title['text'] = "Universo Açaí"
        title['width'] = 15
        title["font"] = ("Helvetica Neue", "35", "bold")
        title.place(x=0, y=0)
        title.pack()
        subtitle = Label(widget1, fg="black", bg="white")
        subtitle['text'] = "O melhor Açaí da Cidade!"
        subtitle['width'] = 20
        subtitle["font"] = ("Helvetica Neue", "12", "italic", "bold")
        subtitle.pack()
        space = Label(widget1, fg="black", bg="white")
        space['text'] = ""
        space['width'] = 20
        space["font"] = ("Helvetica Neue", "12", "italic", "bold")
        space.pack(pady=60)
        loginButton = Button(widget1)
        imgIconRight = ImageTk.PhotoImage(file="img/rigth_icon.png")  
        master.imgIconRight = imgIconRight
        loginButton.config(image= imgIconRight, compound=RIGHT, bg="white")
        loginButton["text"] = "          Entrar          "
        loginButton["font"] = ("Calibri", "15")
        #loginButton["width"] = 50
        loginButton.pack (pady= 10)
        registerButton = Button(widget1)
        imgIconEnter = ImageTk.PhotoImage(file="img/enter_icon.png")  
        master.imgIconEnter = imgIconEnter
        registerButton.config(image= imgIconEnter, compound=RIGHT, bg="#7518B2", fg="white")
        registerButton["text"] = "       Cadastrar       "
        registerButton["font"] = ("Calibri", "15")
        #registerButton["width"] = 5
        registerButton.pack ()
        copy = Label(widget1, fg="#642B8A", bg="white")
        copy['text'] = "©copyright - João Victor Bezerra da Silva - 2º ano de Informatica Matutino"
        copy["font"] = ("Helvetica Neue", "9", "bold")
        copy.place(x=0, y=0)
        copy.pack(pady=90)
        widget1.pack()
        canvas2 = Canvas(w)
        canvas2.configure(bg="white", height=1000, width=900, borderwidth = 0, highlightthickness = 0)
         
        points = [0, 0, 250, 1000, 2000, 1000, 2000,
        0,0,0]
        canvas2.create_polygon(points,  fill='#7518B2')
        canvas2.place(y=-1)
        canvas2.pack(side= RIGHT)
        img = ImageTk.PhotoImage(file="img/acai.png")   
        master.img = img 
        canvas2.create_image(0,50, anchor=NW, image=img)   
        
root = Tk()
Application(root)
root.mainloop()
    

  