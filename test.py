import streamlit as st

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
list=['a','b','c']
st.selectbox('text',list.unique())
