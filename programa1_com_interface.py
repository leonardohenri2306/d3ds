from tkinter import *

janela = Tk()

def bt_click():
    print(ed.get())

#Nome completo
ed = Entry(janela)
ed.place(x= 20, y= 45)
bt = Button(janela, width=3, text = "Ok", command=bt_click)
bt.place(x= 190, y= 40)

#Nome de usuario
ed2 = Entry(janela)
ed2.place(x= 20, y= 90)
bt = Button(janela, width=3, text = "Ok", command=bt_click)
bt.place(x= 190, y= 90)

#Titulos e janelas
janela.title("Register program")
lb3 = Label(janela, text = "Full name")
lb3.place(x= 20, y= 25)

lb4 = Label(janela, text = "User name")
lb4.place(x= 20, y= 69)

lb = Label (janela, text = "Start Register")
lb.place(x=110, y=5)

janela.geometry("300x300+200+200")



janela.mainloop()
