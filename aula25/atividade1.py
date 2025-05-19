from  tkinter import *
from tkinter import simpledialog,messagebox


def dividir_numeros():
    try:
        a = float(simpledialog.askstring("Divisão", "Digite o dividendo:"))
        b = float(simpledialog.askstring("Divisão", "Digite o divisor:"))
        resultado = a / b
        messagebox.showinfo("Resultado", f"Resultado: {resultado}")
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero não é permitida.")
    except Exception as e:
        messagebox.showerror("Erro", f"Entrada inválida: {e}")
def criar_arquivo():
    try:
        with open("arquivo.txt","w") as c:
            c.write(" atividade sobre exception")
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro ao criar o arquivo: {e}")

def ler_arquivo():
    try:
        with open("arquivo.txt", "r") as f:
            conteudo = f.read()
        messagebox.showinfo("Conteúdo do Arquivo", conteudo)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo não encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao ler o arquivo: {e}")
def cadastrar_idade():
    idade_input = simpledialog.askstring("Idade", "Digite sua idade:")
    
    if idade_input is None: 
        return
    
    try:
        idade = int(idade_input)
        if idade < 0:
            messagebox.showerror("Erro", "Idade não pode ser negativa.")
        else:
            messagebox.showinfo("Idade", f"Idade cadastrada: {idade}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um número válido para a idade.")

# Função 4: Simulador de caixa eletrônico
saldo = 20000.0
def sacar():
    valor_input = simpledialog.askstring("Saque", "Digite o valor para saque:")
    
    if valor_input is None:  
        return
    
    try:
        valor = float(valor_input)
        if valor > saldo:
            messagebox.showerror("Erro", "Saldo insuficiente.")
        else:
            saldo -= valor
            messagebox.showinfo("Saque", f"Saque realizado. Saldo atual: R${saldo}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite um valor válido para o saque.")

# Função 5: Verificação de login
usuarios = ["admin", "user", "joao", "leileane", "erickson", "erica"]
def login():
    nome = simpledialog.askstring("Login", "Digite seu nome de usuário:")
    
    if nome is None: 
        return
    
    if nome in usuarios:
        messagebox.showinfo("Login", "Login bem-sucedido.")
    else:
        messagebox.showwarning("Login", "Usuário não encontrado.")

# Função 6: Multiplicação com tratamento de tipo
def multiplicar():
    try:
        a = float(simpledialog.askstring("Multiplicação", "Digite o primeiro número:"))
        b = float(simpledialog.askstring("Multiplicação", "Digite o segundo número:"))
        resultado = a * b
        messagebox.showinfo("Resultado", f"Resultado: {resultado}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao multiplicar: {e}")
 
# Função 7: Abertura de arquivo CSV inexistente
def abrir_csv():
    try:
        with open("dados.csv", "r") as f:
            conteudo = f.read()
        messagebox.showinfo("CSV", conteudo)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo .csv não encontrado.")
 
def calcular_media():
    notas = []
    
    for i in range(3):
        nota_input = simpledialog.askstring("Média", f"Digite a nota {i+1}:")
        
        if nota_input is None: 
            return
        try:
            nota = float(nota_input)
            
            if nota < 0 or nota > 10:
                messagebox.showerror("Erro", "Notas devem estar entre 0 e 10.")
                return 
            notas.append(nota)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um valor válido para a nota.")
            return  
    media = sum(notas) / len(notas)
    messagebox.showinfo("Média", f"Média: {media}")
# Função 9: Acesso a chave inexistente
def acessar_dicionario():
    try:
        dicionario = {"nome": "Carlos", "idade": 30}
        chave = simpledialog.askstring("Dicionário", "Digite a chave a acessar:")
        valor = dicionario[chave]
        messagebox.showinfo("Valor", f"Valor da chave '{chave}': {valor}")
    except KeyError:
        messagebox.showerror("Erro", "Chave não encontrada.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {e}")
 