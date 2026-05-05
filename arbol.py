from stack import stack

class arbolFuncion: 
    def __init__ (self):
        self.cabeza = None
        self.listaImprimible = []
        self.listaCaracteres = ["+", "-", "*", "/", "(",")","^"]
        self.pilaParentesis = stack() # Este stack determina la prioridad de las operaciones
        self.pilaOperaciones = stack() # Este stack tendrá todas las operaciones. [(,+,-),-]
    
        
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
        self.cabeza = self.construirArbolRecursivo(expresion)
        
    def construirArbolRecursivo(self, expresion : str):
        # Primero se recorre la expresion para determinar si hay parentesis redundantes
        self.pilaOperaciones.clear()
        print(f"La expresion es {expresion}")
        for caracter in expresion:
            if caracter in self.listaCaracteres:
                # Si el caracter esta en la lista de caracteres entonces se apila 
                self.pilaOperaciones.push(caracter)
        
        print(self.pilaOperaciones.lista)
        if self.pilaOperaciones.tamano != 0: # Si hay por lo menos una operacion entonces se hace particion
            if self.pilaOperaciones.peek() == ")" and expresion[0] == "(": 
                    # Hay que quitar los parentesis redudantes 
                    expresion = expresion[1:len(expresion)-1]
                    
            #print(expresion)
            for i in range(3):
            # Casos i = 0 Suma/Resta, i = 1 Multiplicacion/Division, i=2 Exponente
                self.pilaParentesis.clear()
                palabra = ""
                banderaSalir = False 
                
                print(f"iteracion: {i}, expresion: {expresion}")
                for j in range(len(expresion)) :
                    # Recoremos la expresion completa
                    caracter = expresion[j] # Caracter actual
                     
                    if i == 0 : # Caso de la suma/resta
                        
                    #Si es suma o resta, la pila esta vacia y no se ha hecho la particion entonces se parte desde ahi
                        if (caracter == "+" or caracter == "-") and self.pilaParentesis.isEmpty():
                            # Se hace particion
                            print(caracter)
                            
                            nuevoNodo = self.nodoArbol(caracter)
                            nuevoNodo.izquierdo = self.construirArbolRecursivo(palabra)
                            nuevoNodo.derecho = self.construirArbolRecursivo(expresion[j+1:])
                            banderaSalir = True # Hubo particion 
                        
                        if banderaSalir: 
                            print(f"Se rompe el ciclo interno")
                            break# Si ya se hizo la particion se rompe el primer ciclo
                        
                        if caracter == "(" :
                            # Si se abre parentesis, entonces las operaciones que vengan despues no "se toman en cuenta"
                            print("Se pushea el (")
                            self.pilaParentesis.push(caracter)
    
                        
                        if caracter == ")" :
                            # Si se cierra parentesis, entonces esas operaciones si "se toman en cuenta"
                            self.pilaParentesis.pop()
                            print("Se hizo pop )")
                        
                        palabra += caracter # Se va armando la palabra
                        
                    if i == 1 : # Caso de la multiplicacion/division
                        
                    #Si es multiplicacion o divison, la pila esta vacia y no se ha hecho la particion entonces se parte desde ahi
                        if (caracter == "*" or caracter == "/") and self.pilaParentesis.isEmpty():
                            # Se hace particion
                            print(caracter)
                            
                            nuevoNodo = self.nodoArbol(caracter)
                            nuevoNodo.izquierdo = self.construirArbolRecursivo(palabra)
                            nuevoNodo.derecho = self.construirArbolRecursivo(expresion[j+1:])
                            banderaSalir = True # Hubo particion 
                        
                        if banderaSalir: 
                            break   # Si ya se hizo la particion se rompe el primer ciclo
                        
                        if caracter == "(" :
                            # Si se abre parentesis, entonces las operaciones que vengan despues no "se toman en cuenta"
                            print("Se pushea el (")
                            self.pilaParentesis.push(caracter)
    
                        
                        if caracter == ")" :
                            # Si se cierra parentesis, entonces esas operaciones si "se toman en cuenta"
                            self.pilaParentesis.pop()
                            print("Se hizo pop )")
                        
                        palabra += caracter # Se va armando la palabra
                
                    if i == 2 : # Caso del exponente 
                        
                    #Si es exponente, la pila esta vacia y no se ha hecho la particion entonces se parte desde ahi
                        if (caracter == "^") and self.pilaParentesis.isEmpty():
                            # Se hace particion
                            print(caracter)
                            
                            nuevoNodo = self.nodoArbol(caracter)
                            nuevoNodo.izquierdo = self.construirArbolRecursivo(palabra)
                            nuevoNodo.derecho = self.construirArbolRecursivo(expresion[j+1:])
                            banderaSalir = True # Hubo particion 
                        
                        if banderaSalir: 
                            break   # Si ya se hizo la particion se rompe el primer ciclo
                        
                        if caracter == "(" :
                            # Si se abre parentesis, entonces las operaciones que vengan despues no "se toman en cuenta"
                            print("Se pushea el (")
                            self.pilaParentesis.push(caracter)
    
                        
                        if caracter == ")" :
                            # Si se cierra parentesis, entonces esas operaciones si "se toman en cuenta"
                            self.pilaParentesis.pop()
                            print("Se hizo pop )")
                        
                        palabra += caracter # Se va armando la palabra
                
                
                if banderaSalir :# Si ya hice una particion se rompe el segundo ciclo
                    break
                
        else:   
            # Si no hay mas operaciones entonces es una x o un numero
            nuevoNodo = self.nodoArbol(expresion)
            
        return nuevoNodo
                                

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
    
    arbolPrueba2 = arbolFuncion()
    arbolPrueba2.construirArbol("x^2+1")
    arbolPrueba2.imprimirArbol()
