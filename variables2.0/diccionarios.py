
#?Creando diccionarios con dict()
diccionario = dict(nombre='matias', apellido='venencio')

#?Las listas no pueden ser claves y usamos frozenset para meter conjuntos (las tuplas si pueden ser claves)
diccionario = {frozenset(['matias', 'rancio']): 'jajasj'}

#?Creando un diccionario con fromkeys() valor pór defecto: None
diccionario = dict.fromkeys('ABCDE', 'Algun valor fijo')

#?Creando diccionario con fromkeys() cambiando el valor por defecto a 'No se'
diccionario = dict.fromkeys(['Nombre', 'Apellido'], 'No se')

 

print(diccionario)