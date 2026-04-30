import math 
import separadores as sp 

def calcularNumero(numero : str):
    # Primero se separaran por sumas y restas en una lista
    resultado = sp.separarSumaResta(numero)
    return resultado 

def identificarFuncion(funcion : str):
    lista = funcion.split()
    
    return lista 

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