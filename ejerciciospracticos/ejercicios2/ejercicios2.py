#creando una funcion que nos devuelva los primos


#crear una funcion verificando si es primo 
def es_primo(num):
    for i in range(2,num-1):
        
        if num%i==0: return False
    return True        

#creando una funcion que retorne  una lsta con todos los primos
def primos(num):
     primos =[]
     for i in range(3,num+1):
        resultado=es_primo(i)
        if resultado==True:primos.append(i)
     return primos


result=primos(13)
print(result)



