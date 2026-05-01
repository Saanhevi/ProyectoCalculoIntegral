class stack :
    lista = 0
    tamano = 0
    def __init__(self): # Constructor de la clase stack
        self.lista = []     # "arreglo" para simular el stack
        self.tamano = 0     # apuntador para el indice 
    
    def push(self, elemento):   # Metodo para apilar un elemento en el stack
        self.lista.append(elemento) 
        self.tamano += 1    # Se incrementa en 1 el apuntador
        
    def pop(self):  # Metodo para desapilar un elemento en el stack
        if self.isEmpty(): 
            print("La pila esta vacia")
            return
        
        valor = self.lista.pop(self.tamano-1)
        self.tamano -= 1    # Se decrementa en 1 el apuntador
        return valor 

    def peek(self): # Metodo para consultar el elemento en la "cima" del stack
        return self.lista[self.tamano-1]
    
    def isEmpty(self): # Metodo para consultar si la pila esta vacia
        return self.tamano == 0
    
    def getTamano(self): # Metodo para obtener el tamano actual de la pila
        return self.tamano

    def clear(self):
        self.lista = []
        
if __name__ == "__main__":
    # Prueba de la implementacion
    pila = stack()
    
    for i in range(5): 
        pila.push(i)
    
    print(f"El tamano es {pila.getTamano()}")
    
    for i in range(pila.getTamano()):
        print(pila.pop())
        
    pila.pop()
    
