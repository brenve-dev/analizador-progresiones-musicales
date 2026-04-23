Base de datos = tu círculo de quintas básico
Cada tonalidad mayor: [I, ii, iii, IV, V, vi, vii°]
tonalidades_mayores = {
"C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
"G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
"D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
"A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
"E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
"F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"]
}

grados_romanos = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]

def analizar_progresion(acordes_usuario):
acordes_usuario = [acorde.strip() for acorde in acordes_usuario.split(" ")]

for tono, acordes_tono in tonalidades_mayores.items():
    grados_encontrados = []
    es_esta_tonalidad = True
    for acorde in acordes_usuario:
        if acorde in acordes_tono:
            indice = acordes_tono.index(acorde)
            grados_encontrados.append(grados_romanos[indice])
        else:
            es_esta_tonalidad = False
            break
    if es_esta_tonalidad:
        return f"Tonalidad: {tono} mayor | Progresión: {' - '.join(grados_encontrados)}"
return "No encontré la tonalidad. Prueba con acordes básicos o agrega más tonalidades al código."

# Agrega esto a tus diccionarios
tonalidades_menores = {
    "Am": ["Am", "Bdim", "C", "Dm", "Em", "F", "G"], # i ii° III iv v VI VII
}
grados_menores = ["i", "ii°", "III", "iv", "v", "VI", "VII"]

PRUEBA AQUÍ: Cambia esta línea
entrada = "G D Em C"
resultado = analizar_progresion(entrada)
print(f"Entrada: {entrada}")
print(f"Resultado: {resultado}")
