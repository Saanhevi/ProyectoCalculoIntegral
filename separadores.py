import identificadores as idn

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
        resultado *= idn.identificarNumero(elemento)
    
    return resultado
    