from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global rep
    rep = 0
    titulo.config(text="Timer", fg= GREEN)
    canvas.itemconfig(texto_timer, text= "00:00") 
    check_mark.config(text="")
    janela.after_cancel(timer)



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    work_min = WORK_MIN *60
    sb_min = SHORT_BREAK_MIN * 60
    lb_min = LONG_BREAK_MIN * 60
    rep += 1
    check = "✅"

    if rep % 2 == 0:
        novo_txt = ""
        n = int(rep /2)
        for _ in range(rep - n):
            novo_txt += check
        
        check_mark.config(text=novo_txt)

    if rep == 1 or rep == 3 or rep == 5 or rep == 7:
        titulo.config(text="Trabalhar", fg= GREEN)      
        contador(work_min)
    elif rep == 2 or rep == 4 or rep == 6:
        titulo.config(text="Descansar", fg= PINK)
        contador(sb_min)
    elif rep == 8:
        titulo.config(text="Descansar", fg= RED)
        contador(lb_min)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def contador(cont):
    global timer
    cont_min = math.floor(cont/60)
    cont_sec = cont %60
    if cont_sec < 10:
        cont_sec = f"0{cont_sec}"

    canvas.itemconfig(texto_timer, text= f"{cont_min}:{cont_sec}")
    if cont > 0:
        timer = janela.after(1000, contador, cont-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
janela = Tk()
janela.title("Pomodoro")
janela.config(padx= 100, pady= 50, bg = YELLOW)


imagem_tomate = PhotoImage(file="Pomodoro/arquivos/tomato.png")
canvas = Canvas(width=200, height= 224, bg= YELLOW, highlightthickness = 0)
canvas.create_image(100, 112, image = imagem_tomate)
texto_timer = canvas.create_text(100, 130, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

titulo = Label(text="Timer", fg= GREEN, bg= YELLOW,font=(FONT_NAME, 35, "bold"))
titulo.grid(column=1, row=0)

start_button, reset_button = Button(text= "Start",width= 5, highlightthickness = 0,command= start_timer), Button(text= "Reset",width= 5, highlightthickness = 0,command= reset_timer)
start_button.grid(column= 0, row= 2)
reset_button.grid(column= 2, row= 2) 

check_mark = Label(fg=GREEN, bg= YELLOW)
check_mark.grid(column=1, row=3)


janela.mainloop()