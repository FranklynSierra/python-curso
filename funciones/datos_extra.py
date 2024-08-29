# def frase(nombre,apellido,adjetivo):
#     print(f'hola{nombre}, tu apellido es{ apellido}, y eres{adjetivo}')
    
    
# #utilizando keyword arguments  
# frase_result=frase(nombre='fran',apellido='sierra',adjetivo='crack')

# print(frase_result)



#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo='crack'):
    print(f'hola{nombre}, tu apellido es{ apellido}, y eres{adjetivo}')
    
    
#utilizando keyword arguments  
frase_result=frase('fran','sierra',adjetivo='cracllll')

print(frase_result)