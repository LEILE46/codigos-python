from tkinter import *
from tkinter import messagebox
from models.pedido import Pedido
from models.item_pedido import ItemPedido
from servicos.salvar import salvar_pedido



class Apptk:
    def __init__(self,janela):
        janela.title("cadastro de itens")
        janela.geometry("900x600")
        janela.config(bg="#900")

        Label(text="informe o nome do cliente:",font=("helvetica",16,"bold"),bg="#900",fg="white").grid(row=0,column=0,sticky="w")
        Label(text="informe o item comprado: ",font=("helvetica",16,"bold"),bg="#900",fg="white").grid(row=1,column=0,sticky="w")
        Label(text="informe a quantidade comprada:",font=("helvetica",16,"bold"),bg="#900",fg="white").grid(row=2,column=0,sticky="w")
        Label(text="informe o preco do produto: ",font=("helvetica",16,"bold"),bg="#900",fg="white").grid(row=3,column=0,sticky="w")
        self.ent_nome=Entry()
        self.ent_item=Entry()
        self.ent_qtd=Entry()
        self.ent_preco=Entry()

        self.ent_nome.grid(row=0,column=1,sticky="w")
        self.ent_item.grid(row=1,column=1,sticky="w")
        self.ent_qtd.grid(row=2,column=1,sticky="w")
        self.ent_preco.grid(row=3,column=1,sticky="w")
        
        Button(text="cadastrar",command=self.salvar_itens).grid(row=4,column=1,sticky="w",columnspan=2)
    def salvar_itens(self):
        nome=self.ent_nome.get()
        item=self.ent_item.get()
        qtd=self.ent_qtd.get()
        preco=self.ent_preco.get()
        if (not nome or not item or not qtd or not preco):
            messagebox.showwarning("atencao","todos os itens deve ser preenchidos!")
            return
        item_pedido=ItemPedido(item,int(qtd),float(preco))
        item_pedido2=ItemPedido("maca",2,20.50)
        pedido1=Pedido(nome,"001","20/05/2025",item_pedido,item_pedido2)

        salvar_pedido(pedido1)
        messagebox.showinfo("cadastro","produto cadastrado com sucesso")