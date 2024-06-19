from Nodo import Nodo
from tkinter.ttk import Treeview

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def get_primero(self):
        return self.primero
    
    def set_primero(self, primero):
        self.primero = primero
        
    def get_ultimo(self):
        return self.ultimo
    
    def set_ultimo(self,ultimo):
        self.ultimo = ultimo
    
    def insertarNodo(self, dato):
        if not self.buscarNodo(dato):
            nodoNuevo = Nodo(dato)
            if self.get_primero() == None:
                self.primero = nodoNuevo
                self.primero.set_siguiente(None)
                self.ultimo=self.primero
                
            else: 
                self.ultimo.set_siguiente(nodoNuevo)
                nodoNuevo.set_siguiente(None)
                self.ultimo=nodoNuevo
                
        else:
            print("Ya existe un dato igual")
        
    def mostrarLista(self):
        nodoActual = self.primero
        listaString = ""
        while nodoActual != None:
            listaString = listaString + str(nodoActual.get_dato()) + "\n"
            nodoActual = nodoActual.get_siguiente()
        return listaString
    
    def buscarNodo(self,dato):
        nodoActual = self.primero
        boolean= False
        while nodoActual != None:
            if nodoActual.get_dato()==dato:
                boolean=True
            nodoActual=nodoActual.get_siguiente()
        return boolean
    
    def modificarNodo(self,datoActual, datoNuevo):
        nodoActual = self.primero
        while nodoActual != None:
            if nodoActual.get_dato()==datoActual:
                nodoActual.set_dato(datoNuevo)
            nodoActual=nodoActual.get_siguiente()
    
    def eliminarNodo(self, dato):
        nodoActual = self.primero
        nodoAnterior = None
        while nodoActual !=None:
            if nodoActual.get_dato()==dato:
                if nodoAnterior==None:
                    self.primero=nodoActual.get_siguiente()
                elif nodoActual.get_siguiente()==None:
                    nodoAnterior.set_siguiente(None)
                else:
                    nodoAnterior.set_siguiente(nodoActual.get_siguiente())
            nodoAnterior=nodoActual
            nodoActual=nodoActual.get_siguiente()
    
    def enlistar(self, tabla: Treeview):
        nodoActual = self.primero
        while nodoActual:
            tabla.insert('','end',values=(nodoActual.get_dato()))
            nodoActual = nodoActual.get_siguiente()
        
        
        