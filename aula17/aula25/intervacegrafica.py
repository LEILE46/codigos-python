from tkinter import *
import atividade1


def main():

    janela=Tk()
    janela.title("excepton")
    janela.geometry("600x400")
    janela.config(background="#524FDA")
    button_divide=Button(text="divisão",width=20,command=atividade1.dividir_numeros)
    button_divide.grid(row=1,column=2,pady=10,padx=10)
    buttonler=Button(text="ler arquivo",width=20,command=atividade1.ler_arquivo)
    buttonler.grid(row=2,column=2,pady=10,padx=5)
    button_criararquivo=Button(text="criar arquivo",width=20,command=atividade1.criar_arquivo)
    button_criararquivo.grid(row=4,column=2,pady=10,padx=5)
    button_cadstro=Button(text="cadastro de idade",width=20,command=atividade1.cadastrar_idade)
    button_cadstro.grid(row=3,column=2,pady=10,padx=5)
    button_caixa=Button(text="caixa eletrônico",width=20,command=atividade1.sacar)
    button_caixa.grid(row=5,column=2,pady=10,padx=5)
    button_login=Button(text=" Verificação de login",width=20,command=atividade1.login)
    button_login.grid(row=6,column=2,pady=10,padx=5)
    button_multiplicar=Button(text=" multiplicar",width=20,command=atividade1.multiplicar)
    button_multiplicar.grid(row=7,column=2,pady=10,padx=5)
    button_abrir_csv=Button(text="abrir arquivo",width=20,command=atividade1.abrir_csv)
    button_abrir_csv.grid(row=8,column=2,pady=10,padx=5)
    button_calcular_media=Button(text=" calcular media",width=20,command=atividade1.calcular_media)
    button_calcular_media.grid(row=9,column=2,pady=10,padx=5)
    button_acessar_dicionario=Button(text="acessar dicionario",width=20,command=atividade1.acessar_dicionario)
    button_acessar_dicionario.grid(row=10,column=2,pady=10,padx=5)

    janela.mainloop()
if __name__== "__main__":
    main()
