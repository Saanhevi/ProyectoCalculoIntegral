from identificadores import calcularNumero

class fnMath :
    diccionarioFactorial = {}
    
    def factorial(n):
        if n==1 or n == 0:
            return 1
        
        # Se verifica si esta en el diccionario y no realizar varias recursiones 
        resultado = fnMath.diccionarioFactorial.get(n,False) 
        
        if not (resultado) : # Si el resultado es falso entonces llama a la funcion
            resultado = n*fnMath.factorial(n-1)
            fnMath.diccionarioFactorial[n] = resultado
            
        return resultado

    
    def seno(x : str):
        x = calcularNumero(x)
        resultado = 0
        
        for n in range(100) : # n va desde 0 a 99
            termino = 1 /(fnMath.factorial(2*n+1))* (x)**(2*n+1)
            
            if n%2 == 0 : # Si n es par, entonces suma 
                resultado += termino
            else:         # Si n es impar, entonces resta
                resultado -= termino
                
        return resultado

    def coseno(x : str): 
        x = calcularNumero(x)
        resultado = 0
        
        for n in range(100) : # n va desde 0 a 99
            termino = 1 /(fnMath.factorial(2*n))* (x)**(2*n)
            
            if n%2 == 0 : # Si n es par, entonces suma 
                resultado += termino
            else:         # Si n es impar, entonces resta
                resultado -= termino
                
        return resultado
        
    def euler():
        resultado = 0
        
        for n in range(100): 
            # e = 1 + 1 + 1/2! + 1/3! + 1/4!
            resultado +=  1/(fnMath.factorial(n))
            
        return resultado
    

    def pi(): 
        # Basado en la serie hipergeometrica generalizada de Ramanujan 
        resultadoSerie = 0
        
        for k in range (5):
            numerador = (fnMath.factorial(6*k))*(13591409+545140134*k)
            denominador = (fnMath.factorial(3*k))*(fnMath.factorial(k)**3)*(640320)**(3*k)
            termino = numerador/denominador
            
            if k%2 == 0: 
                resultadoSerie += termino
            else: 
                resultadoSerie -= termino
        
        return 1/(resultadoSerie*(12/(640320)**(1.5)))


print(fnMath.coseno("pi/2 + 3"))