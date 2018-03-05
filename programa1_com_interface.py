
from tkinter import *

janela = Tk()

def bt_click():
    arquivo = open('dados.txt', 'w')
    arquivo.write("Full name: %s\n" %(fn.get()))
    arquivo.write("User name: %s\n" %(un.get()))
    arquivo.write("individual registration: %s\n" %(cpf.get()))
    arquivo.write("Date of birth: %s\n" %(db.get()))
    arquivo.close()

    print(fn.get())
    print(un.get())
    print(cpf.get())



#Nome completo
fn = Entry(janela, width=50)
fn.place(x= 20, y= 45)
btfn = Button(janela, width=3, text = "Ok", command=bt_click)
btfn.place(x= 430, y= 40)

#Nome de usuario
un = Entry(janela, width=50)
un.place(x= 20, y= 90)
btun = Button(janela, width=3, text = "Ok", command=bt_click)
btun.place(x= 430, y= 90)

#Data de nascimento
db = Entry(janela)
db.place(x= 20, y= 150,)
btdb = Button(janela, width=3, text = "Ok",)
btdb.place(x= 190, y=150)

#cpf
cpf = Entry(janela)
cpf.place(x= 20, y= 200)
btun = Button(janela, width=2, text = "Ok", command=bt_click)
btun.place(x= 190, y=200)

#Titulos e janelas
janela.title("Register program")
lbfn = Label(janela, text = "Full name")
lbfn.place(x= 20, y= 25)

lbun = Label(janela, text = "User name")
lbun.place(x= 20, y= 69)

lb = Label (janela, text = "Start Register")
lb.place(x=110, y=5)

janela.geometry("800x600+300+100")


janela.mainloop()
