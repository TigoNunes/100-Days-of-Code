from tkinter import *

window = Tk()
window.title("Tela de aprendizado")
window.minsize(width= 500, height=300)
# window.config(padx= 20, pady= 20)

# TODO: Rotulo
my_label = Label(text="Rotulo", font = ("Arial", 24, "bold")) 
# Métodos de posicionamento
my_label.pack() #mais estático 
# my_label.place(x=0,y=0) #mais preciso
# my_label.grid(column= 0, row= 0) #meio termo

# Formas alternativas de modificar a variável
## my_label["text"] = "Novo rotulo"
## my_label.config(text= "Novo novo rotulo")
 
# TODO: Button
def button_clicked():
    my_label["text"] = input.get()

button = Button(text= "Botão 1", command= button_clicked)
# button2 = Button(text= "Botão 2", command= button_clicked)
button.pack()
# button.grid(column=1, row=1)
# button2.grid(column=2, row= 0)

# TODO: Entry

input = Entry(width= 10)
input.pack()
# input.grid(column=3, row=2)

# TODO: Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

# TODO: Spinbox
def spinbox_used():
    """gets the current value in spinbox."""
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# TODO: Scale
#Called with current scale value.
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# TODO: Checkbutton
def checkbutton_used():
    """Prints 1 if On button checked, otherwise 0."""
    print(checked_state.get())

#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# TODO: Radiobutton
def radio_used():
    print(radio_state.get())

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# TODO: Listbox
def listbox_used(event):
    """Gets current selection from listbox"""
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop() #TODO: comando que mantem a janela na tela e "escuta" as interações do usuário  

