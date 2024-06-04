import csv
     

def escribir(datos, nombre_archivo):
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)


datos_plantilla = [
    ['Nombre', 'Edad', 'Correo']
]

datos = [
['Nombre', 'Edad', 'Correo'],
['Juan Pérez', '28', 'juan.perez@example.com'],
['María López', '34', 'maria.lopez@example.com'],
['Carlos García', '22', 'carlos.garcia@example.com']
]

 
escribir(datos, 'archivo.csv')
escribir(datos_plantilla, 'archivo.csv')


