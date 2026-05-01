
class stack :
    lista = 0
    tamano = 0
    def __init__(self): 
        self.lista = []
        self.tamano = 0
    
    def push(self, elemento): 
        self.lista.append(elemento)
        self.tamano += 1
        
    def pop(self):
        valor = self.lista.pop(self.tamano-1)
        self.tamano -= 1
        return valor 

    def peek(self):
        return self.lista[self.tamano-1]
    
    
pila = stack()
pila.push("Hola")
pila.push(3)
pila.push(40)

print(pila.peek())
print(pila.pop())
print(pila.pop())