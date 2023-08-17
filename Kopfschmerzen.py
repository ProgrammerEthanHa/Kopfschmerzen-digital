import streamlit as st
import pandas as pd
import altair as alt

st.header("Technik macht Kopfschmerzen")
st.subheader("Beschwerden bei Beschäftigten mit hohem Digitalstress")

source = pd.DataFrame({
        'Prozent(%)': [55, 42, 52, 38, 33],
        'Erkrankung': ['Kopfschmerzen', 'nächtliche Schlafstörungen', 'Müdigkeit, Mattigkeit', 'körperliche Erschöpfung', 'emotionale Erschöpfung']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Prozent(%):Q',
        x='Erkrankung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    /
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Gimpel u.a. 2018")