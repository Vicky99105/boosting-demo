import streamlit as st
from PIL import Image
import base64
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()

visualize = Image.open("./boosting/static/visualization.webp")

"add video here"

st.markdown("""

    #### Summary

    - We use weak learners that are of high bias and low variance.
    - The learners are combined using additive combination
    - In context of regression
        - Scenario:  Instead of predicting loan status, we want to predict for how much amount loan shall be sanctioned
        - Model is build in stages where
            - Stage 0 is mean model
            - Stage 1 model (low depth DT) is built on top of errors (residuals) of stage 0 model
            - Similarly, Stage 2 model  is built on top of errors of stage 1 model… and so on.
            - This continues till Stage M (i.e M models)
    - We also see boosting in context of classification where instead of numerical target variable, we have class and Probability.

    ---

""")

st.markdown("""
    #### Visualizing Boosting

    To solidify the concept, let’s visualize this process of boosting


    """)

file_ = open("./boosting/static/visualize.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="Visualzation" width=700>',
    unsafe_allow_html=True,
)

st.markdown("---")

st.image(visualize)

st.markdown("""
    Incase, you want to see 3D visualization of the procress, visit <a href ="https://arogozhnikov.github.io/2016/06/24/gradient_boosting_explained.html">arogozhnikov blog</a>


""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Why Boosting")
