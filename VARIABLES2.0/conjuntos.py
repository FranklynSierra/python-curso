#creando un conjunto con set

conjunto=set(['dato',('dato2','dato27')])

#metiendo un conjunto dentro de otro conunto

conjunto1=frozenset({'dato1','dato'})
conjunto2={conjunto1,'dato3'}
print(conjunto2)

#teoria de conjuntos 

conjunto1={1,3,5,8}
conjunto2={1,3,7,9,6}
#verificando si es un subconjunto
resultado=conjunto2.issubset(conjunto1)
#da true
print(resultado)

resultado=conjunto2<=conjunto1

print(resultado)

resultado=conjunto2.issuperset(conjunto1)
#da true
print(resultado)

resultado=conjunto2>conjunto1

print(resultado)



#verificar si hay un numero en comun

res=conjunto2.isdisjoint(conjunto1)
print(res)