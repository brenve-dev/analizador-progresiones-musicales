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

progresiones_famosas = {
    "I-V-vi-IV": "Pop-punk / Eje de 4 acordes. Usada en 80% de hits",
    "vi-IV-I-V": "Progresión sensible. Baladas épicas",
    "ii-V-I": "Cadencia jazz por excelencia",
    "I-IV-V-I": "Blues/Rock básico"
}

# Después de obtener grados_encontrados, antes del return:
nombre_progresion = " - ".join(grados_encontrados)
if nombre_progresion in progresiones_famosas:
    info_extra = f"\nDato: {progresiones_famosas[nombre_progresion]}"
    return f"Tonalidad: {tono} mayor | Progresión: {nombre_progresion}{info_extra}"

progresiones_famosas = {
    "I - V - vi - IV": "Eje de 4 acordes. Pop-punk, 80% de hits 2000s",
    "vi - IV - I - V": "Progresión sensible. Baladas épicas tipo 'Someone Like You'",
    "ii - V - I": "Cadencia jazz por excelencia",
    "I - IV - V - I": "Blues/Rock básico. 12-bar blues simplificado",
    "I - vi - IV - V": "50s progression. 'Stand By Me'"
}

def analizar_progresion(acordes_usuario):
    # Ahora acepta minúsculas y espacios extra
    acordes_usuario = [acorde.strip().capitalize() for acorde in acordes_usuario.split()]

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
            nombre_progresion = " - ".join(grados_encontrados)
            resultado = f"Tonalidad: {tono} mayor | Progresión: {nombre_progresion}"

            # Nuevo: detecta si es famosa
            if nombre_progresion in progresiones_famosas:
                resultado += f"\nDato cool: {progresiones_famosas[nombre_progresion]}"

            return resultado

    return "No encontré la tonalidad. Intenta con: C G Am F o G D Em C"
