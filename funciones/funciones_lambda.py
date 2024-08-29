numeros=[1,4,5,7,7,2,58,4,2]
#creando una funcion ñambda para multiplicar  x 2
multiplicar_por_dos=lambda x:x*2

#usando filter con una funcion comun
 
# def es_par(num):
#     if num%2==0:
#         return True

# numeros_pares=filter(es_par,numeros)





#creando lo mismo que antes pero con lambda

numeros_pares=filter(lambda numero:numero%2==0,numeros)




print(list(numeros_pares))