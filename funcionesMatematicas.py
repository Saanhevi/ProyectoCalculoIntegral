class fnMath :
    diccionarioFactorial = {}
    
    def factorial (n):
        if n==1:
            return 1
        
        resultado = fnMath.diccionarioFactorial.get(n,False)
        
        if not (resultado) : # Si el resultado es falso entonces llama a la funcion
            resultado = n*fnMath.factorial(n-1)
            fnMath.diccionarioFactorial[n] = resultado
            
        return resultado

