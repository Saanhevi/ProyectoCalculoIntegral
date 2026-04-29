def identificarFuncion(funcion : str):
    lista = funcion.split()
    
    return lista 
    
def calcularArea(lista, a, b, n):
    acumulador = 0 # Se acumulan las areas 
    indicador_suma_resta = 0        # Si el indicador = 0 se suma, si el indicador = 1 se resta
    for i in range(len(lista)):
        
        if lista[i] == "+" : 
            indicador_suma_resta = 0
        elif lista[i] == "-" :
            indicador_suma_resta = 1
        else:
            # Identificar el coeficiente
            coeficiente = "" # Si queda vacio es un 1
            exponente = "" # Si queda vacio es un 1

            k = 0 # Indice donde termina el coeficiente (K es el indice donde esta x )
            # Conseguir el coeficiente 
            for j in lista[i]:
                if j == "x" :
                    break 
                coeficiente += j # Se va armando el coeficiente 
                k += 1
            
            # Convertimos el coeficiente a un numero 
            if coeficiente == "" :
                coeficiente = 1
            else: 
                coeficiente = int(coeficiente)
            
            if  len(lista[i]) > k+1 and lista[i][k+1] == "^": 
                # k+1 es ^
                # Entonces hay exponente
                for j in range(k+2,len(lista[i])):
                    exponente += lista[i][j] # Se va armando el exponente
                    
            
            # Convertimos el exponente a un numero 
            if len(lista[i]) == k: # Si coincide entonces no hay x
                exponente = 0
            elif exponente == "" : 
                exponente = 1 
            else: 
                exponente = int(exponente)

            area = calcularAreaPorFuncion(a, b, n, exponente, coeficiente) #Area para cada funcion
            
            if indicador_suma_resta == 0: # Si el indicador es igual 0 se suma
                acumulador += area 
            else: # Si el indicador es igual 1 se resta
                acumulador -= area 
    return acumulador
            
def calcularAreaPorFuncion(a, b, n, expo, coef):
    delta_x = (b-a)/n
    xi = a
    yi = 0
    preresultado = 0 
    
    for i in range(1, n): 
        xi = a + i*delta_x
        yi = coef*pow(xi, expo)
        preresultado += yi 
        
    suma_superior = (preresultado + b)* delta_x
    #suma_inferior = (preresultado + a) * delta_x
    
    return suma_superior
    #print(f"La suma superior es {suma_superior}")
    #print(f"La suma inferior es {suma_inferior}")
        
    
    

def main():
    # Se definen los extremos 
    a = int(input("Digite el extremo inferior: "))
    b = int(input("Digite el extremo superior: "))
    
    # Se define el numero de intervalos
    n = int(input("Digite el numero de rectangulos que desea: "))
    
    # Se escribe la funcion (Tiene que ser del tipo ax^n + bx^k, con espacios incluidos)
    funcion = input("Digite la funcion: ")
    lista_funciones = identificarFuncion(funcion)
    resultado = calcularArea(lista_funciones, a, b, n)
    
    print(f"El resultado es: {resultado}")
    # x^2
    # 5x^5 + 10x - 5
    
main()