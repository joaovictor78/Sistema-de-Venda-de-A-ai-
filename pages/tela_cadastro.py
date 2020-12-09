from tkinter import messagebox 
from tkinter import *
from PIL import Image, ImageTk
import re 
class Cadastro(Frame):
    def __init__(self, master):
        validatedName = False
        validatedEmail = False
        validatedPhone = False
        validatedSenha = False
        validatedConfirmarSenha = False
        def popupfunc():
            resp = messagebox.askquestion("Cadastro de usuario",
             "Você concorda com as nossas normas e politicas de privacidade?") 
            print(resp)
        Frame.__init__(self, master)
        master.configure(bg="#7518B2")
        master.iconbitmap ("img/icon_aba1.ico")
        master.title("Universo Açaí - Sabor com qualidade!")
        globalCanvas = Canvas(master, borderwidth = 0, highlightthickness = 0)
        globalCanvas.configure(bg="white")
        globalCanvas.pack(expand="true")
        widget1 = Label(globalCanvas, borderwidth = 0, highlightthickness = 0)
        widget1.configure(bg="white")
        widget1.pack(side=LEFT)
        subtitle = Label(widget1, fg="black", bg="white")
        subtitle['text'] = "Cadastre-se"
        subtitle['width'] = 20
        subtitle["font"] = ("Helvetica", "13","bold")
        subtitle.pack(pady=12)  
        nomeValue = StringVar()
        nome = Entry(widget1, width=70, textvariable=nomeValue)
        nome.configure(fg = 'grey', font = "Arial 10 italic")
        nome.insert(0, ' Digite seu nome')
        nome.bind('<FocusIn>', lambda args: nome.delete('0', 'end'))
        nome.bind('<FocusOut>', lambda args: nome.insert(0, ' Digite seu nome') if nome.get() == '' else "")
        nome.pack(padx=95, pady= 5)
        
        emailValue = StringVar()
        email = Entry(widget1, width=70, textvariable=emailValue)
        email.insert(0, '  Digite seu email')
        email.config(fg='grey', font = "Arial 10 italic")
        email.bind('<FocusIn>', lambda args: email.delete('0', 'end'))
        email.bind('<FocusOut>', lambda args: email.insert(0, ' Digite seu email') if email.get() == '' else "")
        email.pack(pady=5)

        telefoneValue = StringVar()
        telefone = Entry(widget1, width=70, textvariable=telefoneValue)
        telefone.config(fg='grey', font = "Arial 10 italic")
        telefone.insert(0, '  Digite seu telefone')
        telefone.bind('<FocusIn>', lambda args: telefone.delete('0', 'end'))
        telefone.bind('<FocusOut>', lambda args: telefone.insert(0, ' Digite seu Telefone') if telefone.get() == '' else "")
        telefone.pack(pady=5)

        
        senhaValue = StringVar()
        senha = Entry(widget1, width=70, textvariable=senhaValue)
        senha.config(fg='grey', font = "Arial 10 italic")
        senha.insert(0, '  Digite uma senha')
        senha.bind('<FocusIn>', lambda args: senha.delete('0', 'end'))
        senha.bind('<FocusOut>', lambda args: senha.insert(0, ' Digite uma senha') if senha.get() == '' else "")
        senha.pack(pady=5)

        confirmar_senhaValue = StringVar()
        confirmar_senha = Entry(widget1, width=70, textvariable=confirmar_senhaValue)
        confirmar_senha.insert(0, '  Confirme sua senha')
        confirmar_senha.config(fg = 'grey', font = "Arial 10 italic")
        confirmar_senha.bind('<FocusIn>', lambda args: confirmar_senha.delete('0', 'end'))
        confirmar_senha.bind('<FocusOut>', lambda args: confirmar_senha.insert(0, ' Confirme sua senha') if confirmar_senha.get() == '' else "")
        confirmar_senha.pack(pady=5)

        space = Label(widget1, fg="black", bg="white")
        space['text'] = ""
        space['width'] = 20
        space["font"] = ("Helvetica", "12", "italic", "bold")
        space.pack(pady=60)
        registerButton = Button(widget1, command=lambda:validate())
        imgIconEnter = ImageTk.PhotoImage(file="img/enter_icon.png")  
        master.imgIconEnter = imgIconEnter
        registerButton.config(bg="#290628", fg="white")
        registerButton["text"] = "  Cadastrar  "
        registerButton["font"] = ("Calibri", "10")
        registerButton.pack()
        space = Label(widget1, fg="black", bg="white")
        space['text'] = ""
        space['width'] = 20
        space["font"] = ("Helvetica", "5", "italic", "bold")
        space.pack(pady=5)
                   
        def validate():
            if(nome.get() == ' Digite seu nome' or nome.get() == ''):
                nome.delete('0', 'end')
                nome.configure(fg="red")
                nome.insert(0, ' Digite seu nome: *Campo obrigatorio')
                
            else:
                validatedName = True
            if(len(email.get()) < 8):
                email.delete('0', 'end')
                email.configure(fg="red")
                email.insert(0, ' Digite seu email: *Numero minimo de 8 caracteres')
            elif(len(email.get()) > 256):
                email.delete('0', 'end')
                email.configure(fg="red")
                email.insert(0, ' Digite seu email: *Numero maximo de 256 caracteres')
            else:
                validatedEmail = True
            if(re.search(r"(?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$", telefone.get()) == None):
                telefone.delete('0', 'end')
                telefone.configure(fg="red")
                telefone.insert(0, ' Digite seu Telefone Ex:(xx) xxxxx-xxxx *Telefone invalido ')
            else:
                validatedPhone = True
            if(senha.get() == '  Digite uma senha'):
                senha.delete('0', 'end')
                senha.configure(fg="red")
                senha.insert(0, ' Digite uma senha: *Campo obrigatorio')
                
            elif(len(senha.get()) < 5):
                senha.delete('0', 'end')
                senha.configure(fg="red")
                senha.insert(0, ' Digite sua senha: Minimo de 8 caracteres')
            else:
                validatedSenha = True
            if(senhaValue == True and confirmar_senha.get() != senha.get()):
                confirmar_senha.delete('0', 'end')
                confirmar_senha.configure(fg="red")
                confirmar_senha.insert(0, ' Erro: As senhas não coincidem!')
            else:
                validatedConfirmarSenha = True
            if(validatedName == True and validatedEmail == True and validatedPhone == True and validatedSenha == True and validatedConfirmarSenha == True):
                print("Cadastro realizado com sucesso!")
                