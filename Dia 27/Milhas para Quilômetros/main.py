from tkinter import *

janela = Tk()
# janela.minsize(width=500, height= 250)
janela.title("Milhas para Quilômetros")
janela.config(padx=20, pady= 20)

# Entrada

entrada = Entry()
entrada.insert(END, "0")
entrada.config(width = 10)
entrada.focus()
entrada.grid(column= 1, row= 0)

# Botão
def calcula():
    resultado.config(text= round(float(entrada.get()) * 1.609, 2))

botao = Button(text= "Calcular", command= calcula)
botao.grid(column=1, row=2)

# Textos
## é igual
e_igual = Label(text="é igual a:", font = ("Arial", 10, "bold"))
e_igual.grid(column=0, row=1)
# e_igual.config(padx= 10)

## resultado
resultado = Label(text="0", font = ("Arial", 10, "bold"))
resultado.grid(column=1, row=1)
resultado.config(pady= 5)

## KM e Milhas
km, milhas = Label(text="KM", font = ("Arial", 10, "bold")), Label(text="Milhas", font = ("Arial", 10, "bold"))
km.grid(column=2, row= 1)
milhas.grid(column=2, row= 0)
milhas.config(padx= 10)

janela.mainloop()