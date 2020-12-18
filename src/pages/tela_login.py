from tkinter import *
import tela_cadastro, tela_home, requests
import json
from tkinter import messagebox 
url = 'https://delivery-acai-server.herokuapp.com/auth'
class Login(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        master.geometry("1500x900")
        master.configure(bg="white")
        leftContainer = Label(master, bg="#7518B2", width=95, height=1500)
        leftContainer.pack(side=LEFT)
        def navigationPage(page):
            columnWidget.destroy()
            leftContainer.destroy()
            master.switch_frame(page)
        def messageCadastro(resp):
            messagebox.showinfo("Login", resp)
        columnWidget = Label(master, bg= "#7518B2")
        columnWidget.place(x=60, y=150) 

        boasVindasMessage = Label(columnWidget, bg="#7518B2", fg="white")
        boasVindasMessage["text"] = "Bem Vindo!"
        boasVindasMessage["font"] = ("Calibri", "30", "bold")
        boasVindasMessage.grid(row = 0, column = 0, pady = 10)
        emailValue = StringVar()
        email = Entry(columnWidget, width=50, textvariable=emailValue)
        email.insert(0, '  Digite seu email')
        email.config(fg='grey', font = "Calibri 15 italic")
        email.bind('<FocusIn>', lambda args: email.delete('0', 'end'))
        email.bind('<FocusOut>', lambda args: email.insert(0, ' Digite seu email') if email.get() == '' else "")
        email.grid(row = 1, column = 0, sticky = W, pady=10)
        senhaValue = StringVar()
        senha = Entry(columnWidget, width=50, textvariable=senhaValue)
        senha.config(fg='grey', font = "Calibri 15 italic")
        senha.insert(0, '  Digite sua senha')
        senha.bind('<FocusIn>', lambda args: senha.delete('0', 'end'))
        senha.bind('<FocusOut>', lambda args: senha.insert(0, ' Digite uma senha') if senha.get() == '' else "")
        senha.grid(row = 2, column = 0, sticky = W) 
        
        row = Label(columnWidget, bg= "#7518B2")
        row.grid(row = 3, column = 0,  pady = 70) 
        loginButton = Button(row, command=lambda:login(), width=12)
        loginButton.config(bg="#290628", fg="white")
        loginButton["text"] = "  Login  "
        loginButton["font"] = ("Calibri", "12")
        loginButton.grid(row = 3, column = 0,  pady = 2, padx=12) 

        registerButton = Button(row, width=12,   command=lambda: navigationPage(tela_cadastro.Cadastro))
        registerButton.config(bg="white", fg="black")
        registerButton["text"] = "  Criar Conta  "
        registerButton["font"] = ("Calibri", "12")
        registerButton.grid(row = 3, column = 1,  pady = 2) 
        def login():
            jsonLogin = {"email": email.get(), "senha" : senha.get()}
            response = requests.post(url + '/login', json= jsonLogin)
            responseFromJson = json.loads(response.text)
            print(response.text)
            print(response.status_code)
            if(response.status_code == 200):
                token = responseFromJson["token"]
                print(token)
                messageCadastro('Login efetuado com sucesso ' + responseFromJson["user"]["nome"].lower().capitalize() + ' !')
            else:
                messageCadastro(responseFromJson["error"])

    