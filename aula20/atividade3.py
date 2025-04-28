#Crie dois sets de cores. Exiba:
#União dos dois sets
#Interseção dos dois sets
#Diferença entre eles
import tkinter as tk
cores_set1={"azul","laranja","vermelho"}
cores_set2={"roxo","preto","marrom","vermelho"}
janela= tk.Tk()
janela.title("set fruta")
janela.config(background="yellow")
janela.geometry("600x400")
def uniao_cores():
   cores_uniao =cores_set1.union(cores_set2)
   label_cores.config(text=cores_uniao)

def intersecao_cores():
   cores_intersecao=cores_set1.intersection(cores_set2)
   label_cores.config(text=cores_intersecao)
 


def diferença_cores():
   cores_diferença=cores_set1.difference(cores_set2)
   label_cores.config(text=cores_diferença)

   
cores=tk.Label(text=cores_set1)
cores.grid(column=0,row=0)   
cores1=tk.Label(text=cores_set2)
cores1.grid(column=0,row=1)  
botao_uniao = tk.Button(janela, text="exiba unidao das cores ",command=uniao_cores)
botao_uniao.grid(column=1,row=2)
botao_interseçao = tk.Button(janela, text="exiba interseçao das cores ",command=intersecao_cores)
botao_interseçao.grid(column=1,row=3)
botao_diferença = tk.Button(janela, text="exiba deferença das cores ",command=diferença_cores)
botao_diferença.grid(column=1,row=4)

label_cores=tk.Label(janela,text="")
label_cores.grid(column=1,row=5)
janela.mainloop()