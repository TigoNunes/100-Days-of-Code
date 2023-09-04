from tkinter import *
from tkinter import messagebox
from geradorSenhas import GeradorSenha
import pyperclip
import json

# -----------------------Procurar dados------------------------
def procurar_dados():
    try:
        with open("Gerenciador de Senhas/arquivos/dados.json", "r") as dados:
            informacoes = json.load(dados)
    except FileNotFoundError:
        messagebox.showerror(title="Arquivo não encontrado", message= "O arquivo em questão não foi encontrado")
    else:
        nome_site = website_entry.get().title()
        try:            
            messagebox.showinfo(title= nome_site, message=f"Email/Username: {informacoes[nome_site]['email/user name']}\nSenha: {informacoes[nome_site]['senha']}")
        except KeyError:
            messagebox.showerror(title="Site não encontrado", message= f"O site {nome_site} não foi cadastrado")

# -----------------------Gerar senha------------------------
def gerar_senha():
    senha_aleatoria = GeradorSenha()
    senha_entry.delete(0,END)
    senha_entry.insert(0, senha_aleatoria.senha)
    pyperclip.copy(senha_aleatoria.senha) #Faz com que a senha aleatória vá direto para o copiar (Crl+C)
# -----------------------Salvando------------------------
def salvar_arquivos():
    novo_dado = {
        website_entry.get().title():{
            "email/user name": email_username_entry.get(),
            "senha": senha_entry.get(),
        },
    }
    
    if website_entry.get() != "" and senha_entry.get() != "":
        tudo_certo = messagebox.askyesno(title="Confira as informações", message= f"Estes dados estão corretos?\nSite: {website_entry.get()}\nEmail: {email_username_entry.get()}\nSenha: {senha_entry.get()}")
        if tudo_certo:
            try:    
                with open("Gerenciador de Senhas/arquivos/dados.json", "r") as dados:
                    dado = json.load(dados)
                    dado.update(novo_dado)
            except:
                with open("Gerenciador de Senhas/arquivos/dados.json", "w") as dados:    
                    json.dump(novo_dado, dados,indent=4)
            else:
                with open("Gerenciador de Senhas/arquivos/dados.json", "w") as dados:    
                    json.dump(dado, dados,indent=4)
            finally:
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

website_entry = Entry(width= 23)
website_entry.grid(column=1, row=1)
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

# Procurar
procurar = Button(text="Procurar", command= procurar_dados)
procurar.grid(column=2, row=1)

janela.mainloop()