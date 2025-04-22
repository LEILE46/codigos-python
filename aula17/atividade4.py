#Crie uma fila de tarefas. Ao atender uma tarefa (remover da fila), mostre qual foi e quantas ainda restam.
import tkinter as tk
fila_tarefas=[]
def atendendo_tarefas():
    if fila_tarefas:
        tarefa_removida=fila_tarefas.pop(0)
        label_atendendo.config(text=tarefa_removida)
    else:
        label_atendendo.config(text="fila vazia ")

def  adicionar_fila():
    tarefa=entry_tarefa.get()
    fila_tarefas.append(tarefa)
    

janela= tk.Tk()
janela.title("fila de tarefas")

label_atender_tarefa = tk.Label(janela, text="tarefas:")
label_atender_tarefa.pack()

entry_tarefa = tk.Entry(janela)
entry_tarefa.pack(fill="x")
botao_addtarefas=tk.Button (janela,text="adicionar",command=adicionar_fila)
botao_addtarefas.pack(side="left")
botao_adicionar = tk.Button(janela, text="atender tarefas ", command=atendendo_tarefas)
botao_adicionar.pack(side="right")
label_atendendo=tk.Label(janela,text="")
label_atendendo.pack()
janela.mainloop()