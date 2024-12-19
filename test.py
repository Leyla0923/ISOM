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




st.dataframe(data=df)
st.data_editor(df)
st.line_chart(df)
st.table(df)
st.divider()

# Create sample DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
})

# Basic editor
edited_df = st.data_editor(df)

# Advanced editor with customization
edited_df = st.data_editor(
    df,
    num_rows="dynamic",  # Allows adding/deleting rows
    column_config={
        "Name": st.column_config.TextColumn("Full Name"),
        "Age": st.column_config.NumberColumn(
            "Age",
            min_value=0,
            max_value=120
        ),
        "City": st.column_config.SelectboxColumn(
            "City",
            options=["NYC", "LA", "Chicago", "Houston"]
        )
    },
    hide_index=True,
    width=None  # or specific pixel value
)

# Track changes
if edited_df.equals(df):
    st.write("No changes made")
else:
    st.write("Data was modified!")
    st.write("Modified data:", edited_df)

