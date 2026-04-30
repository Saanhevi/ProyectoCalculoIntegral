import identificadores as idn 

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
            lista_coef_k = idn.identificarCoeficiente(lista_funciones[i])
            coeficiente = lista_coef_k[0]
            k = lista_coef_k[1]
            
            # Identificar el exponente
            exponente = idn.identificarExponente(lista_funciones[i], k )
            
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

if __name__ == "__main__":
    print("Hola")
    
