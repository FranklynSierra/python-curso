#2 listas, una con nombres otra con apellidos
 
nombres=['fran','carlos','yeli','roberto']

apellidos=['sierra','jose','contreras','tarado']

#registrar la informacion txt de manera optima

with open('archivos_resolviendo_problemas\\nombres_y_apellidos.txt','w')as arch:
    arch.writelines('los datos son:\n')
    [arch.writelines(f'Nombre: {n}\n Apellido: {a}----------\n')for n,a in zip(nombres,apellidos)]




