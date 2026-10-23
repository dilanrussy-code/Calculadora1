import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")

pantalla = tk.Entry(ventana, font=("Arial", 18))
pantalla.grid(row=0, column=0, columnspan=4)

numero1 = 0
operacion = ""


def calcular(valor):
    global numero1, operacion

    if pantalla.get() == "Error":
        pantalla.delete(0, tk.END)
        numero1 = 0
        operacion = ""

    if valor == "C":
        pantalla.delete(0, tk.END)
        numero1 = 0
        operacion = ""

    elif valor == "D":
        pantalla.delete(len(pantalla.get()) - 1, tk.END)

    elif valor in ["+", "-", "*", "/"]:
        numero1 = float(pantalla.get())
        operacion = valor
        pantalla.delete(0, tk.END)

    elif valor == "=":
        numero2 = float(pantalla.get())

        if operacion == "+":
            resultado = numero1 + numero2
        elif operacion == "-":
            resultado = numero1 - numero2
        elif operacion == "*":
            resultado = numero1 * numero2
        elif operacion == "/":
            if numero2 == 0:
                pantalla.delete(0, tk.END)
                pantalla.insert(0, "Error")
                return
            resultado = numero1 / numero2

        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)

    else:
        pantalla.insert(tk.END, valor)


botones = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "D", "+",
    "="
]

fila = 1
columna = 0

for boton in botones:
    tk.Button(
        ventana,
        text=boton,
        width=5,
        height=2,
        command=lambda x=boton: calcular(x)
    ).grid(row=fila, column=columna)

    columna = columna + 1

    if columna == 4:
        columna = 0
        fila = fila + 1

ventana.mainloop()
