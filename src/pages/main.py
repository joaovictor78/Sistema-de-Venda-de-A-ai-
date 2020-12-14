# 2 ano de Informatica - Matutino
# Joao Victor Bezerra da Silva
# ***** Linguagem de programação *****

from tkinter import *
import tela_home,tela_cadastro


class Application(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(tela_home.Home)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

if __name__ == "__main__":
    app = Application()
    app.iconbitmap("img/icon_aba1.ico")
    app.title("Universo Açaí - Sabor com qualidade!")
    app.mainloop()