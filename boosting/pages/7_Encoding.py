import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()

encoding_1 = Image.open('./static/analysis_4.png')
encoding_2 = Image.open("./static/analysis_2.png")

st.header("Encoding the data")

st.markdown("---")
st.subheader("Encoding Categorical data")

st.image(encoding_1, caption='Bivariate analysis of catgeorical features w.r.t loan_status')


st.markdown('''

Since the cardinality is low, we’ll perform **OHE** for categorical features.

''')

st.markdown("---")

st.subheader("Encoding Numerical data")

st.image(encoding_2, caption='Bivariate analysis of catgeorical features w.r.t loan_status')


st.markdown('''

As numerical features are right skewed, we'll **power transform (log)** them to handle extreme values.

''')

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Modeling")
