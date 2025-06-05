import tkinter as tk
from tkinter import messagebox
from models.usuario import Usuario
from view.app import tela_principal 

def autenticar_usuario(nome, senha):
    usuario = Usuario(nome) 
    usuario.carregar_dados() 
    if usuario.verificar_senha(senha):
        return True
    return False

def tela_login():
    def tentar_login():
        nome = entry_nome.get()
        senha = entry_senha.get()
        if autenticar_usuario(nome, senha):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            root.destroy()  
            tela_principal(nome)  
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    root = tk.Tk()
    root.title("Login Águas Guariroba")

    root.config(bg="#4CAF50")  

    tk.Label(root, text="Usuário:", fg="white", bg="#4CAF50", font=("Arial", 12)).pack(pady=10)
    entry_nome = tk.Entry(root, font=("Arial", 12))
    entry_nome.pack(pady=5)

    tk.Label(root, text="Senha:", fg="white", bg="#4CAF50", font=("Arial", 12)).pack(pady=10)
    entry_senha = tk.Entry(root, show="*", font=("Arial", 12))
    entry_senha.pack(pady=5)

    tk.Button(root, text="Entrar", bg="#3e8e41", fg="white", font=("Arial", 12), command=tentar_login).pack(pady=20)

    root.mainloop()