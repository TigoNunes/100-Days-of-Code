from tkinter import *
from tkinter import messagebox
from geradorSenhas import GeradorSenha
import pyperclip
import json

# -----------------------Gerar senha------------------------
def gerar_senha():
    senha_aleatoria = GeradorSenha()
    senha_entry.delete(0,END)
    senha_entry.insert(0, senha_aleatoria.senha)
    pyperclip.copy(senha_aleatoria.senha) #Faz com que a senha aleatória vá direto para o copiar (Crl+C)
# -----------------------Salvando------------------------
def salvar_arquivos():
    # Caso algum campo esteja vazio o programa alertará erro
    if website_entry.get() != "" and senha_entry.get() != "":
        tudo_certo = messagebox.askyesno(title="Confira as informações", message= f"Estes dados estão corretos?\nSite: {website_entry.get()}\nEmail: {email_username_entry.get()}\nSenha: {senha_entry.get()}")
        if tudo_certo:    
            with open("Gerenciador de Senhas/arquivos/dados.txt", "a") as dados:
                dados.write(f"{website_entry.get()} | {email_username_entry.get()} | {senha_entry.get()}\n")
            website_entry.delete(0, END)
            senha_entry.delete(0, END)
    else: messagebox.showerror(title="Campos não preenchidos", message= "Todos os campos devem ser preenchidos")
       
# -----------------------UI------------------------
janela = Tk()
janela.title("Gerenciador de senhas")
janela.config(padx=25, pady= 25, bg= "White")

imagem_cadeado = PhotoImage(file= "Gerenciador de Senhas/arquivos/logo.png")
canvas = Canvas(width= 200, height= 200, bg= "White", highlightthickness=0)
canvas.create_image(100, 100, image = imagem_cadeado)
canvas.grid(column=1, row=0)

# Website
website = Label(text="Website:", font=("Arial", 12, "bold"), bg= "White")
website.grid(column=0, row=1)

website_entry = Entry(width= 35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username
email_username = Label(text="Email/Username:", font=("Arial", 12, "bold"), bg= "White")
email_username.grid(column=0, row=2)

email_username_entry = Entry(width= 35)
email_username_entry.insert(END, "@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)

# Senha
senha = Label(text="Senha:", font=("Arial", 12, "bold"), bg= "White")
senha.grid(column=0, row=3)

senha_entry = Entry(width= 23)
senha_entry.grid(column=1, row=3)

senha_button = Button(text="Gerar senha", command= gerar_senha)
senha_button.grid(column=2, row=3)
# senha_button.config(padx= 10)

# Adicionar
adicionar = Button(text="Adicionar", width=36, command=salvar_arquivos)
adicionar.grid(column=1, row=4, columnspan=2)

janela.mainloop()