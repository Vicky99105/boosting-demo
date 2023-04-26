import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()

fi = Image.open("./static/fi.jpg")
fi_plot = Image.open("./static/fi_plot.jpg")


st.header("Model Interpretation using various techniques")


st.markdown("""
    ---

    #### How do we find feature importance in boosting models ?

    Hint: <a href="https://scikit-learn.org/stable/modules/ensemble.html#feature-importance-evaluation">
    sklearn Feature importance evaluation</a>

    Feel free to explore the resources on internet.
""", unsafe_allow_html=True)


answer = st.text_area(
    "Type out your thoughts in text box below and Submit using Ctrl + Enter")

if(answer):

    st.markdown(f"""
        #### Your thoughts:
    """)
    st.write(answer)

    st.markdown(
        f"""



        #### Here's what your peers think:

        **Vishal**:

        - Calculate for each tree and average

        **Vicky**

        - Take weighted average of each tree's feature importance based on their contribute in reducing error.

        ---
    """
    )

    st.markdown("""
        #### Conclusion:

        We do it by averaging the feature importance of a particular feature across all trees.  (we did in RF)


        #### Feature Importance using sklearn

        Let’s see how sklearn provides us with Feature importance

        <a href = "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier.decision_function">sklearn GBDT documentation</a>

    """, unsafe_allow_html=True)

    code = "gbdt.feature_importances_"

    st.code(code, 'python', line_numbers=True)

    st.image(fi)

    st.image(fi_plot)


st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Issues")
