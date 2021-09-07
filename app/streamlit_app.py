import streamlit as st
import requests

#with st.echo():
st.write('# Substract two numbers:')
url = f'https://minimal-production-code-3jzq5a6kpq-ew.a.run.app/dif'
first_number  = st.text_input('first number: ', '5')
second_number = st.text_input('second number: ', '7')


params = {
    'a' : first_number,
    'b' : second_number
}
response = requests.get(url, params=params)

st.write(response.status_code)
st.json(response.json())
st.write(type(response.json()))
st.write(response.json()["a-b"])

