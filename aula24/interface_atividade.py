from tkinter import *
import atividade1

def main():

    janela=Tk()
    janela.title("dicionario")
    janela.geometry("600x400")
    janela.config(background="purple")


    frame_label=Frame(janela,background="lightblue",padx=10,pady=10,height=5)
    frame_label.grid(row=2,column=3,)

    botao_adicionar=Button( text="Adicionar", width=20, command=atividade1.adicionar_contato)
    botao_adicionar.grid(row=0, column=0, padx=5,pady=5)
    botao_agenda = Button(janela, text="Adicionar Compromisso", width=20, command=atividade1.adicionar_compromisso)
    botao_agenda.grid(row=1, column=0, padx=5, pady=5)
    botao_media_preco = Button(janela, text="Calcular Média de Preços", width=20, command=atividade1.calcular_media_preco)
    botao_media_preco.grid(row=2, column=0, padx=5, pady=5)
    botao_remover=Button(text="remover produtos baratos",width=20,command=atividade1.remover_produtos_baratos)
    botao_remover.grid(row=3,column=0,padx=5, pady=5)
    botao_verifica_chave=Button(janela, text="verificar chave", width=20, command=atividade1.verificar_chave)
    botao_verifica_chave.grid(row=4,column=0)
    botao_cadastrar=Button(janela,text="cadastrar aluno",width=20,command=atividade1.cadastrar_aluno)
    botao_cadastrar.grid(row=5,column=0,pady=5,padx=5)
    botao_atualizar_veiculo=Button(janela,text="atualizar veiculo",width=20,command=atividade1.atualizar_veiculo)
    botao_atualizar_veiculo.grid(row=6,column=0,pady=5,padx=5)
    botao_calcular_pedido=Button(janela,text="calcular pedido",width=20,command=atividade1.calcular_pedido)
    botao_calcular_pedido.grid(row=7,column=0,pady=5,padx=5)
    botao_simular_boletim=Button(janela,text="simular boletim",width=20,command=atividade1.simular_boletim)
    botao_simular_boletim.grid(row=8,column=0,pady=5,padx=5)


    label_produtos = Label(frame_label, text="Produtos Disponíveis: produto1': 12.5,'produto2': 8.5,'produto3': 15.0,'produto4': 5.0", bg="lightblue",font=( "Arial",8))
    label_produtos.grid(column=3, row=2)
    janela.mainloop()
if __name__== "__main__":
    main()
