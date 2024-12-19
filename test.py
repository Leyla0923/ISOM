import streamlit as st
import pandas as pd

st.title("hello")
st.write('# hello')
st.divider()
st.header('hello')
st.write('## hello')
st.divider()
st.subheader('hello')
st.write('### hello')
st.divider()
st.text('hello')
st.write('hello')


st.divider()


st.caption('text')
df = pd.DataFrame({'a':[12],'b':[14]})




st.dataframe(data=df, width=None, height=None)
