
#?Creando un conjunto con set()
conjunto = set(['Dato 1', 'Dato 2'])

#?Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['dato1', 'dato2'])
conjunto2 = {conjunto1, 'dato3'}
print(conjunto2)

#?Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

#?Verificando si es un subconjunto con issubset() y con <=
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#?Verificando si es un subconjunto con issubset() y con <=
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto1 > conjunto2

#?Verificar si hay algun resultado en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)