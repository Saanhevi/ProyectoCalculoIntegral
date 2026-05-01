class arbolBinario: 
    # Arbol para representar la funcion 
    
    def __init__ (self): # valor : str
        self.tamano = 0
        self.cabeza = None
        listaImprimible = []
        #self.cabeza = self.nodoArbol(valor)
         
    
    class nodoArbol:
        # Clase para crear objetos tipo Nodo, necesario para crear el arbol
        valor = 0
        
        def __init__(self, valor: str):
            self.valor = valor # Valor de ese nodo
            self.izquierdo = None  # Apuntador al hijo izquierdo 
            self.derecho = None    # Apuntador al hijo derecho 
            
        def getValor(self):
            return self.valor 
    
    def agregar(self, valor):
        # Se llama a la funcion que va a recurrir
        self.cabeza = self.agregarNodo(valor, self.cabeza)
        self.tamano += 1
    
    def agregarNodo(self, valor, nodo):
        # Cuando llega a un "nodo null" ahi debe colocar el valor
        if nodo == None :
            nuevoNodo = self.nodoArbol(valor)
            return nuevoNodo
        
        if nodo.getValor() < valor :
            # Si el valor a agregar es mayor, entonces se va a la derecha
            nodo.derecho = self.agregarNodo(valor, nodo.derecho)
        else: 
            # Si el valor a agregar es menor o igual, entonces se va a la izquierda
            nodo.izquierdo = self.agregarNodo(valor, nodo.izquierdo)
            
        return nodo 
    
    def imprimirArbol(self):
        # Se vacia la listaImprimible
        self.listaImprimible = []
        
        # Se llama a la funcion que imprime cada uno de los nodos
        self.imprimirArbolNodo(self.cabeza)
        print(self.listaImprimible)
        
    def imprimirArbolNodo(self, nodo):
        # Esta forma de imprimir es in-order, por lo que los numeros estaran en orden 
        if nodo == None: 
            return 
        
        # Primeramente trae el valor izquierdo 
        valorIzquierdo = self.imprimirArbolNodo(nodo.izquierdo)

        if valorIzquierdo is not None: 
            # Si no dio None al retornar (Hay un elemento) entonces se agrega
            self.listaImprimible.append(valorIzquierdo)

        # Se guarda el valor del nodo actual, el cual siempre tendra un elemento
        self.listaImprimible.append(nodo.valor)
        
        # Luego se trae el valor del nodo derecho
        valorDerecho = self.imprimirArbolNodo(nodo.derecho)
        
        if valorDerecho is not None: 
            # Si no dio None al retornar (Hay un elemento) entonces se agrega
            self.listaImprimible.append(valorDerecho)


if __name__ == "__main__":
    
    # Casos de prueba para el arbol binario
    arbolPrueba = arbolBinario()
    arbolPrueba.agregar(5)
    arbolPrueba.agregar(7)
    arbolPrueba.agregar(10)
    arbolPrueba.agregar(2)
    arbolPrueba.agregar(3)
    arbolPrueba.agregar(1)
    arbolPrueba.imprimirArbol()