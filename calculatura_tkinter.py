
from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("300x300")

Label(ventana, text="Primer numero").pack()
n1 = Entry(ventana)
n1.pack()

Label(ventana, text="Segundo numero").pack()
n2 = Entry(ventana)
n2.pack()

Label(ventana, text="Resultado").pack()
res = Entry(ventana)
res.pack()

def sumar():
    res.delete(0, END)
    res.insert(0, float(n1.get()) + float(n2.get()))

def restar():
    res.delete(0, END)
    res.insert(0, float(n1.get()) - float(n2.get()))

def multiplicar():
    res.delete(0, END)
    res.insert(0, float(n1.get()) * float(n2.get()))

def dividir():
    res.delete(0, END)
    if float(n2.get()) != 0:
        res.insert(0, float(n1.get()) / float(n2.get()))
    else:
        res.insert(0, "Error")

Button(ventana, text="Sumar", command=sumar).pack()
Button(ventana, text="Restar", command=restar).pack()
Button(ventana, text="Multiplicar", command=multiplicar).pack()
Button(ventana, text="Dividir", command=dividir).pack()

ventana.mainloop()
