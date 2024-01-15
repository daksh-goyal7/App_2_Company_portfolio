import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("Accenture private limited")
content = """Accenture plc is an Irish-American professional services company based in Dublin, specializing in information
 technology (IT) services and consulting. A Fortune Global 500 company, it reported revenues of $64.1 billion in 2023. 
 Accenture's current clients include 91 of the Fortune Global 100 and more than three-quarters of the Fortune Global 500
 . As of 2022, Accenture is considered the largest consulting firm in the world by number of employees."""
st.write(content)
st.subheader("Our Team")
col1, col2, col3 = st.columns(3)
df = pandas.read_csv("company_page/data.csv")
with col1:
    for index, rows in df[:4].iterrows():
        st.subheader(f'{rows["first name"].title()}  {rows["last name"].title()}')
        st.write(rows["role"])
        st.image("company_page/images/" + rows["image"])
with col2:
    for index, rows in df[4:8].iterrows():
        st.subheader(f'{rows["first name"].title()}  {rows["last name"].title()}')
        st.write(rows["role"])
        st.image("company_page/images/" + rows["image"])
with col3:
    for index, rows in df[8:12].iterrows():
        st.subheader(f'{rows["first name"].title()}  {rows["last name"].title()}')
        st.write(rows["role"])
        st.image("company_page/images/" + rows["image"])
