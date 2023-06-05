
# ? Creando una funcion simple
# def saludar():
    # print('Hola Matias, mi maestro ¿Como andas?')
    
#* Ejecutando la funcion simple
# saludar()

#* Creando una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif (sexo == 'hombre'):
        adjetivo = 'rei'
    else:
        adjetivo = 'amor'
        
    print(f'Hola {nombre}, mi {adjetivo} ¿Como andas?')
    
saludar('Juana', 'MuJER')