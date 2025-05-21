from tela.interface import Interface
import tkinter as tk

def main():
    janela = tk.Tk() 
    interface = Interface(janela) 
    janela.mainloop() 

if __name__ == "__main__":
    main()