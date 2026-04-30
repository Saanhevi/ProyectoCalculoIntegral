import math 
import identificadores as idn
import riemann as rmn

def main():
    # Se definen los extremos
    # Se pueden incluir numeros "especiales" como pi y e 
    # Se puede incluir restas y sumas dentro de los limites como pi + 5
    # Se pueden incluir multiplicaciones y divisiones como 5*pi y pi/2
    # Las sumas y restas se separan por espacio y multiplicaciones y divisiones van al lado del numero
    # Se pueden incluir decimales con punto como 7.142 (Coeficientes y limites) 
    a = idn.calcularNumero(input("Digite el extremo inferior: "))
    b = idn.calcularNumero(input("Digite el extremo superior: "))
    
    # Se define el numero de intervalos
    n = 10000
    #n = int(input("Digite el numero de rectangulos que desea: "))
     
    # Se escribe la funcion (Tiene que ser del tipo ax^n + bx^k, con espacios incluidos)
    funcion = input("Digite la funcion: ")
    lista_funciones = idn.identificarFuncion(funcion)
    resultado = rmn.calcularArea(lista_funciones, a, b, n)
    # 
    print(f"La suma superior es: {resultado[0]} \nLa suma inferior es: {resultado[1]}")
    # x^2
    # 5x^5 + 10x - 5
    
main()