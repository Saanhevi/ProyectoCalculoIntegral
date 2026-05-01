from identificadores import calcularNumero

class fnMath :
    diccionarioFactorial = {}
    
    def factorial(n):
        if n==1:
            return 1
        
        # Se verifica si esta en el diccionario y no realizar varias recursiones 
        resultado = fnMath.diccionarioFactorial.get(n,False) 
        
        if not (resultado) : # Si el resultado es falso entonces llama a la funcion
            resultado = n*fnMath.factorial(n-1)
            fnMath.diccionarioFactorial[n] = resultado
            
        return resultado

    
    def seno(x):
        x = calcularNumero(x)
        resultado = 0
        
        for n in range(100) : # n va desde 0 a 49
            termino = 1 /(fnMath.factorial(2*n+1))* (x)**(2*n+1)
            
            if n%2 == 0 : # Si n es par, entonces suma 
                resultado += termino
            else:         # Si n es impar, entonces resta
                resultado -= termino
                
        return resultado
print(fnMath.seno("pi/2 + pi"))