#Simule uma fila de impressão de documentos. Cada documento tem um nome. Ao imprimir, remova o primeiro.
import tkinter as tk
fila_impressao=["documento1","documento2","documento3","documento4"]

def imprimir_documento():
    if len(fila_impressao)>0:
        impresso= fila_impressao.pop(0)
        resultado_label.config(text=f"o documento {impresso}foi impresso")
    else:
        resultado_label.config(text="foi todos os documentos")

    


janela=tk.Tk()
janela.title("fila de documentos")
janela.config(background="green")
janela.geometry("600x400")
for documento in fila_impressao:
    lbdocumento=tk.Label(janela,text=documento).pack()

imprimir_button = tk.Button(janela, text="imprimir resultado", command=imprimir_documento)
imprimir_button.pack(pady=5)

 
resultado_label = tk.Label(janela, text=f"", bg="white")
resultado_label.pack(pady=20)

janela.mainloop()
