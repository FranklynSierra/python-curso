#creando la serie fibonacci 


def fibonacci(num):
    a,b=0,1
    lista=[0]
    
    for i in range(num):
         if b>num:return lista
         else:
             lista.append(b)
             a,b=b,a+b
     

res=fibonacci(82)
print(res)

