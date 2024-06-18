import csv

def leer_equipos(nombre_archivo):
    equipos = {}
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            grupo, equipo = fila[0], fila[1]
            if grupo not in equipos:
                equipos[grupo] = {}
            equipos[grupo][equipo] = {'Puntos': 0, 'PartidosJugados': 0, 'Victorias': 0, 'Empates': 0, 'Derrotas': 0, 'GolesAFavor': 0, 'GolesEnContra': 0, 'DiferenciaDeGoles': 0}
    return equipos

def leer_partidos(nombre_archivo):
    partidos = []
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            partidos.append({'Match Number': int(fila[0]), 'Home Team': fila[1], 'Away Team': fila[2], 'Home Team Goals': 0, 'Away Team Goals': 0})
    return partidos

def actualizar_resultados(nombre_archivo, equipos, partidos):
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if len(fila) != 3:
                print(f"Formato incorrecto en la fila: {fila}")
                continue
            try:
                match_number = int(fila[0])
                home_team_goals = int(fila[1])
                away_team_goals = int(fila[2])
            except ValueError:
                print(f"Datos no válidos en la fila: {fila}")
                continue
            
            for partido in partidos:
                if partido['Match Number'] == match_number:
                    partido['Home Team Goals'] = home_team_goals
                    partido['Away Team Goals'] = away_team_goals
                    actualizar_posiciones(equipos, partido)
                    break

def actualizar_posiciones(equipos, partido):
    home_team = partido['Home Team']
    away
