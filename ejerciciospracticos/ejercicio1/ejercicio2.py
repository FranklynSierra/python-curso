# texto=list([])
# mostrando el dato
# texto.extend(input('dame una frase'))

# print(f'dijiste un total de palabras de {texto}')

frase=input('dame una frase')
cantidad_palabras=frase.split(' ')

valortotal=len(cantidad_palabras)
valordalto=len(cantidad_palabras)

persona_promedio=valortotal/2
print(persona_promedio)

dalto=valordalto/2/1.3
print(dalto)


if valortotal>120:
    print(f'epa te pasaste, tu toal es de {cantidad_palabras}')
else:
    print(f'tu candtifad es de {cantidad_palabras}')    