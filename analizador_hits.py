import pandas as pd
import streamlit as st

st.title("Detector de Fórmulas de Hits 🎵📊")
st.write("Análisis de patrones en canciones top")

# Simulación: después esto viene de Spotify real
data = {
    'cancion': ['Ojitos Lindos', 'Tití Me Preguntó', 'Provenza', 'Efecto', 'Moscow Mule',
                'As It Was', 'Anti-Hero', 'Flowers', 'Calm Down', 'Shakira BZRP'],
    'artista': ['Bad Bunny', 'Bad Bunny', 'Karol G', 'Bad Bunny', 'Bad Bunny',
                'Harry Styles', 'Taylor Swift', 'Miley Cyrus', 'Rema', 'Bizarrap'],
    'progresion': ['I-V-vi-IV', 'i-VI-III-VII', 'I-V-vi-IV', 'vi-IV-I-V', 'I-V-vi-IV',
                   'I-V-vi-IV', 'vi-IV-I-V', 'I-V-vi-IV', 'vi-IV-I-V', 'i-VI-III-VII'],
    'bpm': [100, 106, 111, 98, 100, 173, 97, 118, 105, 122],
    'tono': ['C', 'Am', 'G', 'Em', 'D', 'A', 'C', 'Am', 'F#m', 'Gm'],
    'modo': ['Mayor', 'Menor', 'Mayor', 'Menor', 'Mayor', 'Mayor', 'Mayor', 'Menor']
}

df = pd.DataFrame(data)

st.header("1. ¿Qué progresión domina los charts?")
prog_count = df['progresion'].value_counts()
st.bar_chart(prog_count)
st.write(f"Ganadora: **{prog_count.index[0]}** aparece en {prog_count.iloc[0]} de {len(df)} canciones")

st.header("2. ¿A qué velocidad van los hits?")
st.write(f"BPM promedio: **{df['bpm'].mean():.0f}** | Rango: {df['bpm'].min()}-{df['bpm'].max()}")
st.line_chart(df['bpm'])

st.header("3. Mayor vs Menor")
modo_count = df['modo'].value_counts()
st.bar_chart(modo_count)

st.header("4. Insight automático")
mayor_prog = prog_count.index[0]
if mayor_prog == 'I-V-vi-IV':
    st.success("PATRON DETECTADO: El 'Eje Pop-Punk' sigue dominando. 4 de 4 acordes mayores = sonido alegre/comercial")
