import streamlit as st
st.title('Data Analysis for Automotive Industry')
st.header("kuch bhi")
st.subheader("The following steps are involved in the analysis")
st.text("1. Data Cleaning\n 2. Visualization\n 3. Insights")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:
** bold **
_ italics _
""",True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')
d ={
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
} 
st.write(d)