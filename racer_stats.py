import streamlit as st
import pandas as pd
st.markdown("# Racer Page 🎈")
st.sidebar.markdown("# This is Racer Page 🎈")

st.write(' # Mariokart *Stats Website*')

df_racer = pd.read_csv('data/racer_stats.csv')

# st.write(df_racer)

st.dataframe(df_racer.style
.highlight_max(color='lightgreen', axis=0,subset=['Speed','Acceleration','Weight'])
.highlight_min(color='red', axis=0,subset=['Speed','Acceleration','Weight']))

st.line_chart(df_racer,x='Speed',y='Acceleration')

st.header("Racer Speed does not seem to correlate to number of races they win")
x=st.slider('How many racers to Show',1,len(df_racer))

st.write('Racers by Speed')