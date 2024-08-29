#creando una funcion simple

def saluda(a):
    print(a*8)
    
#efecutando una funcion simple
saluda('hola')    


#creando una funcion con un parametro


def saludar(hola,sexo):
    sexo=sexo.lower()
    if(sexo=='mujer'):
        print(f'{hola},profesora')
    else:
        print(f'{hola}, profesor')
        
    
   

saludar('fran','mujer')




#crear una funcion que  retorne multiples valores
def contraseña_radndom(num):
   caracteres='abcdefhitgfhththjiar6'
   num_entero=str(num)
   num=int(num_entero[0])
   c1=num-2
   c2=num
   c3=num-5
   contraseña=f'{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{num_entero*2}'
  
   return contraseña,num 

#desempaquetando la funcion
contraseña,numero=contraseña_radndom(564)

#mostrando los resultadors obtenidos
print(f'tu contraseña es: {contraseña} y el numero que usaste fue {numero}')


