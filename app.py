import streamlit as st

# Tu mismo código de antes va aquí 👇
tonalidades_mayores = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"]
}

grados_romanos = ["I", "ii", "iii", "IV", "V", "vi", "vii°"]

progresiones_famosas = {
    "I - V - vi - IV": "Eje de 4 acordes. Pop-punk, 80% de hits 2000s",
    "vi - IV - I - V": "Progresión sensible. Baladas épicas tipo 'Someone Like You'",
    "ii - V - I": "Cadencia jazz por excelencia",
    "I - IV - V - I": "Blues/Rock básico. 12-bar blues simplificado",
    "I - vi - IV - V": "50s progression. 'Stand By Me'"
}

def analizar_progresion(acordes_usuario):
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
            resultado = f"**Tonalidad:** {tono} mayor\n**Progresión:** {nombre_progresion}"
            if nombre_progresion in progresiones_famosas:
                resultado += f"\n\n**Dato cool:** {progresiones_famosas[nombre_progresion]}"
            return resultado
    return "No encontré la tonalidad. Prueba con: C G Am F"

# INTERFAZ WEB - Esto es lo nuevo 👇
st.title("Analizador de Progresiones Musicales 🎵")
st.write("Pega tus acordes separados por espacios y te digo en qué tono estás")

entrada = st.text_input("Tus acordes:", "C G Am F")

if st.button("Analizar"):
    if entrada:
        resultado = analizar_progresion(entrada)
        st.success(resultado)
    else:
        st.warning("Escribe algunos acordes primero")

st.markdown("---")
st.caption("Hecho con Python + Streamlit por Brenve desde Mazatlán 🇲🇽")
