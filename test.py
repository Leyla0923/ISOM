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
df = pd.DataFrame({'a':[12,1,2,3,4],'b':[14,3,4,5,4]})
st.dataframe(df)

st.table(df)
st.divider()
st.markdown('---')

st.button("submit")

st.markdown('1. textttttt\n2. sdknklsdsdlksd\n3. sdkjkjfsd')
st.markdown('- hello\n- no hello')
st.divider()
with st.form(key='form'):
  a =st.text_input("Gmail")
  b= st.form_submit_button("Submit")
  if b:
    if not a:
        st.error("error")
    else:
      st.success('success')

