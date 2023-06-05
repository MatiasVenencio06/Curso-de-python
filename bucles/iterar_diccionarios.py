diccionario = {
    'nombre': 'Matias',
    'apellido': 'Venencio',
    'edad': 20
}

for key in diccionario:
    key
    print(f"La clave es: {key}")

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es {key} y el valor {value}')