numeros = [4, 7, 1, 42]

#? Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros) #? Si hay algun string en la lista, diccionario o tupla, devuelve una excepcion
print(numero_mas_alto)

#? Encontrando el numero menor de una lista
numero_mas_bajo = min(numeros) #? Si hay algun string en la lista, diccionario o tupla, devuelve una excepcion
print(numero_mas_bajo)

#? Redondeando a 6 decimales
numero = round(12.345435, 2)

#? Retorna False -> 0, vacio, False, None || True -> distinto a 0, True, cadena, datos no vacios
resultado_bool = bool(0)

#? Retorna True, si todos los valores son verdaderos
resultado_all_false = all([False, 3242, 'sdadas', ['dsd']]) #* Esto daria False ya que no todos los datos son tipo 'True'
resultado_all_true = all([True, 3242, 'sdadas', ['dsd']]) #* Estao daria True ya que todos los datos son tipo 'True'p 


#? Suma todos los valores de un iterable
suma_total = sum(numeros) #? Si hay algun string en la lista, diccionario o tupla, devuelve una excepcion


print(suma_total)
print(numero)