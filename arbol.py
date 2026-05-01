from stack import stack

class arbolFuncion: 
    def __init__ (self):
        self.cabeza = None
        self.listaImprimible = []
        self.listaCaracteres = ["+", "-", "*", "/", "(",")","^"]
        self.pilaParentesis = stack()
        self.pilaOperaciones = stack()
    
        
         
    class nodoArbol:
        # Clase para crear objetos tipo Nodo, necesario para crear el arbol
        
        def __init__(self, valor: str):
            self.valor = valor # Valor de ese nodo
            self.izquierdo = None  # Apuntador al hijo izquierdo 
            self.derecho = None    # Apuntador al hijo derecho 
            
    
    def imprimirArbol(self):
        # Se vacia la listaImprimible
        self.listaImprimible = []
        
        # Se llama a la funcion que imprime cada uno de los nodos
        self.imprimirArbolRecursivo(self.cabeza)
        print(self.listaImprimible)
        
    def imprimirArbolRecursivo(self, nodo : nodoArbol):
        # Esta forma de imprimir es in-order, por lo que los numeros estaran en orden 
        if nodo == None: 
            return 
        
        # Primeramente trae el valor izquierdo 
        valorIzquierdo = self.imprimirArbolRecursivo(nodo.izquierdo)

        if valorIzquierdo is not None: 
            # Si no dio None al retornar (Hay un elemento) entonces se agrega
            self.listaImprimible.append(valorIzquierdo)

        # Se guarda el valor del nodo actual, el cual siempre tendra un elemento
        self.listaImprimible.append(nodo.valor)
        
        # Luego se trae el valor del nodo derecho
        valorDerecho = self.imprimirArbolRecursivo(nodo.derecho)
        
        if valorDerecho is not None: 
            # Si no dio None al retornar (Hay un elemento) entonces se agrega
            self.listaImprimible.append(valorDerecho)

    def construirArbol(self, expresion : str):
        self.cabeza = self.construirArbolRecursivo(self.cabeza, expresion)
        
    def construirArbolRecursivo(self, nodo : nodoArbol, expresion : str):
        # Primero se recorre la expresion para determinar si hay parentesis redundantes
        self.pilaOperaciones.clear()
        
        for caracter in expresion:
            if caracter in self.listaCaracteres:
                # Si el caracter esta en la lista de caracteres entonces se apila 
                self.pilaOperaciones.push(caracter)
        
        print(self.pilaOperaciones.lista)# Si no esta vacio
        if self.pilaOperaciones.peek() == ")" : 
                # Hay que quitar los parentesis redudantes 
                expresion = expresion[1:len(expresion)-1] 

        for i in range(3):
            # Casos i = 0 Suma/Resta, i = 1 Multiplicacion/Division, i=2 Exponente
            self.pilaParentesis.clear()
            palabra = ""
            banderaSalir = False 
             
            if banderaSalir : # Si ya hice una particion se rompe el ciclo 
                break
            for j in range(len(expresion)) :
                
                if i == 0 : # Caso de la suma/resta
                    caracter = expresion[j] # Caracter actual
                    # Si es suma o resta y la pila esta vacia entonces se parte desde ahi
                    if (caracter == "+" or caracter == "-") and self.pilaParentesis.isEmpty():
                        # Se hace particion
                        nodo = self.nodoArbol(caracter)
                        nodo.izquierdo = self.construirArbolRecursivo(nodo.izquierdo, palabra)
                        nodo.derecho = self.construirArbolRecursivo(nodo.derecho, expresion[j+1:])
                        banderaSalir = True # Hubo particion 
                        
                    if caracter == "(" :
                        # Si se abre parentesis, entonces las operaciones que vengan despues no "se toman en cuenta"
                        self.pilaParentesis.push(caracter)
                        print("Se hizo push")
                    
                    if caracter == ")" :
                        # Si se cierra parentesis, entonces esas operaciones si "se toman en cuenta"
                        self.pilaParentesis.pop()
                        print("Se hizo pop")
                    
                    palabra += caracter # Se va armando la palabra

        
        if not banderaSalir: # Si no hubo particion entonces esta ahi quedaria
            nodo = self.nodoArbol(expresion)
            
        return nodo  
                    

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
    
    # arbolPrueba.imprimirArbol()
    
    arbolPrueba2 = arbolFuncion()
    arbolPrueba2.construirArbol("x+2")
    arbolPrueba2.imprimirArbol()
