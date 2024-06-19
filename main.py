#Práctica de Listas Enlazadas de la clase 6 Semana U

from tkinter import *
from customtkinter import *
from tkinter.ttk import Treeview, Style
from ListaEnlazada import ListaEnlazada


LISTA = ListaEnlazada()
CONTADOR = 1
root = CTk()
root.title('Menú de tiquetes')
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}+{-10}+{0}')

def ingresar_ticket():
    global CONTADOR, LISTA
    LISTA.insertarNodo(CONTADOR)
    CONTADOR += 1
    recargar()
    
def atender():
    global LISTA
    if LISTA.get_primero():
        numero = LISTA.get_primero().get_dato()
        print("Atendiendo a", numero)
        LISTA.eliminarNodo(numero)
        atendiendo.configure(text=f"{numero}")
        recargar()
        root.after(1000, atender)
    else: 
        atendiendo.configure(text="Esperando tiquetes")
        
def terminar():
    root.destroy()

CTkButton(master=root, text='Ticket', command=ingresar_ticket).grid(row=1, column=0, padx=100, pady=50)

tvStyle = Style()
tvStyle.configure('Treeview.Heading',font=('Calibri', 16))
tvStyle.configure('Treeview',font=('Calibri', 15))
tabla_clientes = Treeview(master=root, columns=['Tiquete'], show='headings')
tabla_clientes.heading('Tiquete', text='Clientes por atender')
tabla_clientes.column('Tiquete',anchor=CENTER)
tabla_clientes.grid(row=1, column=1, padx=100, pady=30)

def recargar():
    tabla_clientes.delete(*tabla_clientes.get_children())
    #.LISTA.enlistar(tabla_clientes)
    nodoActual = LISTA.get_primero()
    while nodoActual:
        tabla_clientes.insert('','end',values=(nodoActual.get_dato()))
        nodoActual = nodoActual.get_siguiente()
  
CTkLabel(master=root,text="Atendiendo a:").grid(row=1, column=2, padx=100, pady=30, sticky=N)
atendiendo=CTkLabel(master=root, text="Esperando tiquetes")
atendiendo.grid(row=1, column=2, padx=100)
CTkButton(master=root, text='Empezar a atender', command=atender).grid(row=1, column=2, sticky=S)
        
root.protocol('WM_DELETE_WINDOW',terminar)
run = True

root.mainloop()
run = False
