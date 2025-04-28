#Desafio: Crie dois sets de alunos de dois cursos diferentes. Exiba os alunos que estão nos dois cursos (interseção) e os que são exclusivos de cada curso (diferença).
import tkinter as tk
curso_engenharia={}
curso_engenharia=set(curso_engenharia)
curso_mecanica={}
curso_mecanica=set(curso_mecanica)

def adicionar_aluno_engenharia():
    aluno_engenharia=entry_menu.get()
    curso_engenharia.add(aluno_engenharia)
    label_engenharia.config(text=curso_engenharia)
def adicionar_aluno_mecanica():
    aluno_mecanica=entry_menu.get()
    curso_mecanica.add(aluno_mecanica)
    label_mecanica.config(text=curso_mecanica)
def exibi_intersecao():
    intersecao=curso_engenharia.intersection(curso_mecanica)
    label_intercecao.config(text=intersecao)
def exibi_diferença():
    diferenca=curso_engenharia.difference(curso_mecanica)
    diferenca2=curso_mecanica.difference(curso_engenharia)
    label_alunos_diferença_mecanica.config(text=diferenca2)
    label_diferença_aluno_engenharia.config(text=diferenca)

janela= tk.Tk()
janela.title("set numeros")
janela.config(background="purple")
janela.geometry("600x400")
entry_menu = tk.Entry(janela)
entry_menu.grid(column=0,row=1)

botao_intersecao = tk.Button(janela, text="exiba interseçao dos alunos no cursos",command=exibi_intersecao)
botao_intersecao.grid(column=1,row=5)
botao_exibi_diferença=tk.Button(janela,text="exibi diferença dos alunos no curso ",command=exibi_diferença)
botao_exibi_diferença.grid(column=1,row=4)
botao_adicionar=tk.Button(janela,text="adicionar alunos no curso engenharia",command=adicionar_aluno_engenharia)
botao_adicionar.grid(column=1,row=2)
label_engenharia=tk.Label(text="")
label_engenharia.grid(column=2,row=2)
botao_adicionar_aluno_mecanica=tk.Button(janela,text="adicionar aluno no curso mecanica",command=adicionar_aluno_mecanica)
botao_adicionar_aluno_mecanica.grid(column=1,row=3)
label_mecanica=tk.Label(text="")
label_mecanica.grid(column=2,row=3)

label_intercecao=tk.Label(text="")
label_intercecao.grid(column=2,row=5)

label_alunos_diferença_mecanica=tk.Label(janela,text="")
label_alunos_diferença_mecanica.grid(column=3,row=4)
label_diferença_aluno_engenharia=tk.Label(janela,text="")
label_diferença_aluno_engenharia.grid(column=2,row=4)

janela.mainloop()