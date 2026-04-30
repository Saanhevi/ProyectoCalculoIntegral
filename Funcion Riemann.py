import math 

def identificarFuncion(funcion : str):
    lista = funcion.split()
    
    return lista 

def calcularNumero(numero : str):
    # Primero se separaran por sumas y restas en una lista
    resultado = separarSumaResta(numero)
    return resultado 

def separarSumaResta(numero : str):
    lista_numeros_operadores = numero.split()   # ["2*pi/2", "+", "50"]
    indicador_suma_resta = 0 # 0 <-- suma, 1 <-- resta
    resultado = 0
    
    for elemento in lista_numeros_operadores: 
        
        # Se suma el elemento (numero) siempre y cuando no sea un operador
        if indicador_suma_resta == 0 and elemento != "-" and elemento != "+": 
            resultado += separarMultiplicacion(elemento)
        
        # Se resta el elemento (numero) siempre y cuando no sea un operador
        if indicador_suma_resta == 1 and elemento != "-" and elemento != "+":
            resultado -= separarMultiplicacion(elemento)

        if elemento == "+" : 
            indicador_suma_resta = 0
        if elemento == "-": 
            indicador_suma_resta = 1
            
    return resultado

def separarMultiplicacion(numero : str): 
    lista_numeros_operador = numero.split("*") # ["2", "pi/2"]
    resultado = 1
    # Se llama a la funcion identificadora para que deje de ser de tipo string
    for elemento in lista_numeros_operador:
        if elemento == "":
            continue
        resultado *= identificarNumero(elemento)
    
    return resultado
    
    
def identificarNumero(numero : str): 
    es_negativo = False
    
    if numero[0] == "-" :
        es_negativo = True
        numero = numero[1:]
    
    # Identificar si es un decimal
    if "." in numero :
        numero = float(numero)    
    # Identificar si es una fraccion
    elif "/" in numero :
        numerador, denominador = numero.split("/")
        numerador = identificarNumero(numerador)
        denominador = identificarNumero(denominador)
        numero = numerador/denominador
    # Identificar si es un numero especial
    elif "pi" in numero :
        numero = math.pi 
    elif "e" in numero : 
        numero = math.e 
    # Sino entonces es un entero
    else: 
        numero = int(numero)
    
    if es_negativo :
        numero *= -1
    
    return numero 
    

def identificarCoeficiente(subfuncion : str):
    # Identificar el coeficiente 
    coeficiente = "" # Si queda vacio es un 1
    k = 0 # Indice donde termina el coeficiente (K es el indice donde esta x )
    
    # Conseguir el coeficiente 
    for caracter in subfuncion : 
        if caracter == "x" : 
            break 
        coeficiente += caracter # se va armando el coeficiente
        k += 1
    
    # Se convierte el coeficiente a un numero
    if coeficiente == "" : 
        coeficiente = 1
    else: 
        coeficiente = calcularNumero(coeficiente)
        
    return [coeficiente, k] # Lista con el coeficiente y con la posicion donde esta el x (indice k)

def identificarExponente(subfuncion : str , k : int):
    exponente = ""
    if len(subfuncion) > k+1 and subfuncion[k+1] == "^" : 
        # k+1 es ^
        # Entonces hay exponente
        exponente = "" # Si queda vacio es un 1 o 0
        for i in range(k+2, len(subfuncion)):
            exponente += subfuncion[i] # Se va armando el exponente
            
    
    if len(subfuncion) == k: # Si coincide entonces no hay x
        exponente = 0
    elif exponente == "" :
        exponente = 1
    else :
        exponente = calcularNumero(exponente) 
    
    return exponente


def calcularArea(lista_funciones : list, a : int, b : int, n : int):
    acumulador = [0,0] # Se acumulan las areas ( indice = 0 suma superior, indice = 1 suma inferior)
    indicador_suma_resta = 0        # Si el indicador = 0 se suma, si el indicador = 1 se resta
    for i in range(len(lista_funciones)):
        
        if lista_funciones[i] == "+" : 
            indicador_suma_resta = 0
        elif lista_funciones[i] == "-" :
            indicador_suma_resta = 1
        else:
            # Identificar el coeficiente
            lista_coef_k = identificarCoeficiente(lista_funciones[i])
            coeficiente = lista_coef_k[0]
            k = lista_coef_k[1]
            
            # Identificar el exponente
            exponente = identificarExponente(lista_funciones[i], k )
            
            lista_areas = calcularAreaPorFuncion(a, b, n, exponente, coeficiente) #Area para cada funcion
            
            if indicador_suma_resta == 0: # Si el indicador es igual 0 se suma
                acumulador[0] += lista_areas[0]
                acumulador[1] += lista_areas[1]  
            else: # Si el indicador es igual 1 se resta
                acumulador[0] -= lista_areas[0]
                acumulador[1] -= lista_areas[1]
                
    return acumulador # Lista con las areas inferiores y superiores
            
def calcularAreaPorFuncion(a : int, b : int, n : int, expo : int, coef : int):
    # Funcion que calcula la suma de riemman para una funcion del tipo ax^b
    delta_x = (b-a)/n
    xi = a
    yi = 0
    preresultado = 0 
    
    for i in range(1, n): 
        xi = a + i*delta_x
        yi = coef*pow(xi, expo)
        preresultado += yi 
        
    suma_superior = (preresultado + coef*pow(b,expo))* delta_x
    suma_inferior = (preresultado + coef*pow(a, expo)) * delta_x
    
    return [suma_superior, suma_inferior]
        

def main():
    # Se definen los extremos
    # Se pueden incluir numeros "especiales" como pi y e 
    # Se puede incluir restas y sumas dentro de los limites como pi + 5
    # Se pueden incluir multiplicaciones y divisiones como 5*pi y pi/2
    # Las sumas y restas se separan por espacio y multiplicaciones y divisiones van al lado del numero
    # Se pueden incluir decimales con punto como 7.142 (Coeficientes y limites) 
    a = calcularNumero(input("Digite el extremo inferior: "))
    b = calcularNumero(input("Digite el extremo superior: "))
    
    # Se define el numero de intervalos
    n = 10000
    #n = int(input("Digite el numero de rectangulos que desea: "))
     
    # Se escribe la funcion (Tiene que ser del tipo ax^n + bx^k, con espacios incluidos)
    funcion = input("Digite la funcion: ")
    lista_funciones = identificarFuncion(funcion)
    resultado = calcularArea(lista_funciones, a, b, n)
    # 
    print(f"La suma superior es: {resultado[0]} \nLa suma inferior es: {resultado[1]}")
    # x^2
    # 5x^5 + 10x - 5
    
main()