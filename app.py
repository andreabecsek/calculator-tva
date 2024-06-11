import streamlit as st
st.set_page_config(page_title="Pret cu TVA",layout="centered")
st.title("Calculator de pret cu TVA")

with st.form("my_form"):
    without_vat = st.number_input("Introduceti suma fara TVA")
    st.form_submit_button('Calculeaza')
with_vat = str(without_vat*1.19)
st.write("Suma cu TVA de 19 \% adaugat este ", with_vat)
