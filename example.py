import os

import requests

URL = 'http://127.0.0.1:5000/'

opcion = ''
while opcion != '0':
    opcion = input('Opción: ')
    match opcion:
        case '1':
            # Login superadmin (1)
            r = requests.get(f'{URL}/login?identificador=0&password=UAgCZ646D5l9Vbl')
            print(r.status_code)
            token = r.text
            print(token)

        case '2':
            # Crear usuario (2)
            r = requests.post(
                f'{URL}/usuario?identificador=12345&nombre=Miguel&apellido1=Teruel&apellido2=Martinez&password=zCWlAusK*7BfFy',
                headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '3':
            # Buscar usuario (3)
            r = requests.get(f'{URL}/usuario?identificador=12345', headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '4':
            # Crear libro (4)
            r = requests.post(
                f'{URL}/libro?isbn=9781492056355&titulo=Fluent Python 2nd Edition&autor=Luciano Ramalho&'
                f'editorial=O\'Reilly Media, Inc.&anyo=2022',
                headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '5':
            # Buscar libro (5)
            r = requests.get(f'{URL}/libro?isbn=9781492056355')
            print(r.status_code)
            print(r.text)

        case '6':
            # Crear préstamo (6)
            r = requests.post(f'{URL}/prestamo?isbn=9781492056355&identificador=12345',
                              headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '7':
            # Login usuario (7)
            r = requests.get(f'{URL}/login?identificador=12345&password=zCWlAusK*7BfFy')
            print(r.status_code)
            token = r.text
            print(token)

        case '8':
            # Devolver libro (8)
            r = requests.delete(f'{URL}/prestamo?isbn=9781492056355',
                                headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '9':
            # Actualizar libro (9)
            r = requests.put(
                f'{URL}/libro?isbn=9781492056355&titulo=Fluent Python 3rd Edition&autor=Luciano Ramalho&'
                f'editorial=O\'Reilly Media, Inc.&anyo=2022',
                headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '10':
            # Eliminar libro (10)
            r = requests.delete(f'{URL}/libro?isbn=9781492056355', headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '11':
            # Actualizar usuario (11)
            r = requests.put(f'{URL}/usuario?&nombre=Miguel Angel&apellido1=Teruel&apellido2=Martinez',
                             headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '12':
            # Cambiar contraseña (12)
            r = requests.put(f'{URL}/cambiar_password?old_password=zCWlAusK*7BfFy2&new_password=zCWlAusK*7BfFy2',
                             headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '13':
            # Eliminar usuario (13)
            r = requests.delete(f'{URL}/usuario?identificador=12345', headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '14':
            # Subir carátula (14)
            r = requests.post(f'{URL}/caratula?isbn=9781492056355', headers={'Authorization': 'Bearer ' + token},
                              files={'file': open('/Users/miji/Desktop/fluent.jpg', 'rb')})
            print(r.status_code)
            print(r.text)

        case '15':
            # Bajar carátula (15)
            r = requests.get(f'{URL}/caratula?isbn=9781492056355')
            print(r.status_code)
            if r.status_code == 200:
                open("caratula.jpg", "wb").write(r.content)

        case '16':
            # Añadir libro por ISBN (16)
            r = requests.post(f'{URL}/libro?isbn=9780545798631', headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            print(r.text)

        case '17':
            # Bajar carátula (17)
            r = requests.get(f'{URL}/exportar')
            print(r.status_code)
            if r.status_code == 200:
                open("biblioteca.zip", "wb").write(r.content)

        case '18':
            # Generar carné (18)
            r = requests.get(f'{URL}/carne', headers={'Authorization': 'Bearer ' + token})
            print(r.status_code)
            if r.status_code == 200:
                open("carne.pdf", "wb").write(r.content)

        case '19':
            # Generar ficha (19)
            r = requests.get(f'{URL}/ficha?isbn=9781589770089')
            print(r.status_code)
            if r.status_code == 200:
                open("ficha.pdf", "wb").write(r.content)

        case '20':
            # Generar informe préstamos (20)
                r = requests.get(f'{URL}/informe_prestamos', headers={'Authorization': 'Bearer ' + token})
                print(r.status_code)
                if r.status_code == 200:
                    open("prestamos.pdf", "wb").write(r.content)
