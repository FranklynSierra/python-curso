#AND

Resultado = True & True #Devolver True
Resultado2 = False & True #Devolver Falso
Resultado3 = True & False #Devolver Falso
Resultado4 = False & False #Devolver Falso

#OR

Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultado7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT

Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True

pagar=45
total=50

if pagar>40 & total <=50:
    print('tienes lo suficiente')
elif pagar>=45 & total<=50:
    print('te queda justo')    
elif pagar==45 & pagar<45:
    print('te falta dinero')
    
print(Resultado9)
