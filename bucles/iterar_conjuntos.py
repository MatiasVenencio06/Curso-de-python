animales = ['perro', 'gato', 'loro', 'cocodrilo']
numeros = (10, 62, 12, 72)

#?Recorriendo la conjunto animales
for animal in animales: 
    print(animal)
    

#?Recirriendo la conjunto numeros y multiplicando los nimeros por 10
for numero in numeros:  
    resultado = numero * 10
    print(resultado)
    
    
#?Iterando dos conjuntos del mismo tamaño al mismo tiempo
for numero, animal in zip(animales, numeros):
    print(animal, numero)
    
#?Forma no optima de recorrer una conjunto
for num in range(5, 10):
    print(num)
    
#?Forma correcta de recorrer una conjunto con su indice
for num in enumerate(numeros):
    print(num[1])
    
#?Usando el else
for numero in numeros:
    print(f'ejecutando el ultimo bluce, vaor actual: {numero}')
else:
    print('el bucle termino')
    
    
#!LO ANTERIOR FUNCIONA TAMBIEN PAR ITERAR TUPLAS Y CONJUNTOS