#Criar dicionário de contatos (nome: telefone).
# Criar agenda de compromissos por data.
# Exibir o valor médio dos preços em um dicionário de produtos.
# Remover todos os produtos com valor abaixo de R$10.
# Verificar se uma chave existe no dicionário usando in.
# Criar um sistema de cadastro de alunos com nome, nota e status.
# Dicionário com dados de um veículo (marca, modelo, ano) e permitir atualizar os dados.
# Usar values() para somar todas as quantidades do estoque.
# Criar cardápio e calcular total da compra com base em itens escolhidos.
# Simular um boletim escolar com disciplinas e médias, mostrando aprovação/reprovação.
from tkinter import *
from tkinter import messagebox,simpledialog
contatos={}
agenda={}
produtos = {
    'produto1': 12.5,
    'produto2': 8.5,
    'produto3': 15.0,
    'produto4': 5.0
}
alunos = {}
veiculo = {'marca': 'Toyota', 'modelo': 'Corolla', 'ano': 2020}
estoque = {
    'item1': 10,
    'item2': 5,
    'item3': 20
}
cardapio = {
    'Pizza': 30,
    'Hamburguer': 15,
    'Refrigerante': 5
}
boletim = {}

def adicionar_contato():
    nome=simpledialog.askstring("contato","nome")
    telefone=simpledialog.askstring("contato","telefone")
    if nome and telefone:
        contatos[nome]=telefone
        messagebox.showinfo("sucesso",f"{contatos}")
    else:
        messagebox.showerror("erro"," preencha ambos os campos!😐")


def adicionar_compromisso():
    data = simpledialog.askstring("Agenda", "Digite a data (DD/MM/AAAA):")
    compromisso = simpledialog.askstring("Agenda", "Digite o compromisso:")
    if data and compromisso:
        agenda[data] = compromisso
        messagebox.showinfo("Sucesso", f"Compromisso em {data} adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Por favor, preencha ambos os campos!")
def calcular_media_preco():
    if produtos:
        media_preco = sum(produtos.values()) / len(produtos)
        messagebox.showinfo("Média de Preços", f"A média de preços dos produtos é: R${media_preco}")
    else:
        messagebox.showerror("Erro", "Não há produtos cadastrados!")

def remover_produtos_baratos():
    produtos_filtrados = {}
    for produto in produtos:
        if produtos[produto] >= 10:
            produtos_filtrados[produto] = produtos[produto]
    messagebox.showinfo("Produtos Filtrados", f"Produtos com preço acima de R$10: {produtos_filtrados}")

def verificar_chave():
    chave = simpledialog.askstring("Verificar Chave", "Digite o nome para verificar se existe no dicionário de contatos:")
    if chave in contatos:
        messagebox.showinfo("Chave Encontrada", f"A chave '{chave}' existe no dicionário.")
    else:
        messagebox.showerror("Chave Não Encontrada", f"A chave '{chave}' não foi encontrada no dicionário.")

def cadastrar_aluno():
    nome = simpledialog.askstring("Cadastro de Aluno", "Digite o nome do aluno:")
    nota = simpledialog.askfloat("Cadastro de Aluno", "Digite a nota do aluno:")
    if nome and nota is not None:
        status = 'Aprovado' if nota >= 7 else 'Reprovado'
        alunos[nome] = {'nota': nota, 'status': status}
        messagebox.showinfo("Sucesso", f"Aluno {nome} cadastrado com sucesso! Status: {status}")
    else:
        messagebox.showerror("Erro", "Por favor, preencha ambos os campos!")

def atualizar_veiculo():
    marca = simpledialog.askstring("Atualizar Veículo", "Digite a nova marca do veículo:")
    modelo = simpledialog.askstring("Atualizar Veículo", "Digite o novo modelo do veículo:")
    ano = simpledialog.askstring("Atualizar Veículo", "Digite o novo ano do veículo:")
    if marca and modelo and ano:
        veiculo['marca'] = marca
        veiculo['modelo'] = modelo
        veiculo['ano'] = ano
        messagebox.showinfo("Sucesso", f"Veículo atualizado: {veiculo}")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
def calcular_pedido():
    total = 0
    pedido = []
    while True:
        item = simpledialog.askstring("Cardápio", f"Escolha um item:\n{cardapio}\nDigite 'fim' para encerrar.")
        if item is None or item == 'fim':
            break
        if item in cardapio:
            total += cardapio[item]
            pedido.append(item)
        else:
            messagebox.showerror("Erro", "Item não encontrado no cardápio.")
    if pedido:
        messagebox.showinfo("Pedido Finalizado", f"Itens: {pedido}\nTotal: R${total}")
    else:
        messagebox.showinfo("Pedido Vazio", "Nenhum item selecionado.")

def simular_boletim():
    nome = simpledialog.askstring("Boletim", "Nome do aluno")
    if not nome:
        messagebox.showerror("Erro", "Nome inválido.")
        return
    disciplinas = {}
    while True:
        materia = simpledialog.askstring("Disciplina", "Nome da disciplina (ou 'fim' para encerrar)")
        if materia is None or materia == 'fim':
            break
        try:
            media = float(simpledialog.askstring("Média", f"Média final em {materia}:"))
            disciplinas[materia] = media
        except:
            messagebox.showerror("Erro", "Insira uma média válida.")
    resultado = ""
    for d, m in disciplinas.items():
        status = "Aprovado ✅" if m >= 7 else "Reprovado ❌"
        resultado += f"{d}: {m} - {status}\n"
    boletim[nome] = disciplinas
    messagebox.showinfo("Boletim", f"Aluno: {nome}\n{resultado}")
