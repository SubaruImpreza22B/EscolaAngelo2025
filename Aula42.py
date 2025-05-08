import tkinter as tk
from tkinter import messagebox as msg

Janela = tarefa = ListaBox = None

def adicionar():
    novaTarefa = tarefa.get()
    if novaTarefa:
        ListaBox.insert(tk.END, novaTarefa)
        tarefa.delete(0, tk.END)
    else:
        msg.showwarning("Aviso", "Digite uma tarefa") 

def concluir():
    item = ListaBox.curselection()
    if item:
        ListaBox.delete(item)
        msg.showinfo("Concluído", f"tarefa {item[]} concluída")



def interface():
    global tarefa, ListaBox

    rotulo = tk.Label(Janela, text="Tarefa")
    rotulo.pack(pady=10)

    tarefa = tk.Entry(Janela, width=70)
    tarefa.pack(pady=(0, 10), padx=20)

    bt_adicionar = tk.Button(Janela, text="Adicionar tarefa", command=adicionar)
    bt_adicionar.pack(pady=10)
    ListaBox = tk.Listbox(Janela, width=70, height=10)
    ListaBox.pack(padx= 20, pady=10)

    bt_concluir = tk.Button(Janela, text="Concluir", command=concluir)
    bt_concluir.pack(pady=10)

def main():
    Janela = tk.Tk()
    Janela.title("gerenciador de tarefas")
    interface()
    Janela.mainloop()
main()