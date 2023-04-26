import streamlit as st
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()


st.markdown("""

    #### We already have RF which is faster to train (tree parallelization) compared to boosting, why is boosting used then ?

    The magic of boosting is that we can **minimize any differentiable loss** using **Gradient Boosting**

    - Instead of calculating residuals, we calculate **pseudo residual** at each stage (using derivative)

    - These pseudo residuals help us in minimizing any loss we want.

    ---

    Let’s understand step by step how gradient boosting works (pseudo code)

    **add video here**

    ---
""")

st.markdown("""
    ####  Based on what we have learnt so far, what do you think are hyperparams used to train GBDT ?

""")

options = [
    "number of estimators",
    "Learning rate",
    "Depth of tree",
    "Criterion",
    "Mininmum samples to split node on",
    "Min samples in leaf",
    "Max depth",
    "Max number of leaf nodes",
    "col sampling",
    "number of neighbours"
]

selected = st.multiselect("", options)

selected = ", ".join(selected)


if st.button('Submit'):
    st.markdown(f"""
        #### Your response:

        **{selected}**

        ---

        #### Your peers response:

        **Raghav**:  Number of estimators, max depth, learning rate

        **Anant**: Number of estimators, max depth, learning rate, Mininmum samples to split on, Min samples in leaf

        **Vicky**: Number of estimators, learning rate, Mininmum samples to split on, Min samples in leaf, Criterion

        ---

        #### Answer:

        The major hyperparams are:

        - **Number of estimators**
        - **Learning rate**
        - **Depth of tree**
        - **Criterion**
        - **Min_samples_split**
        - **Min_samples_leaf**
        - **Max_depth**
        - **Max_leaf_nodes**

        Here's
        <a href = "https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html">
        sklearn documentation for GBDT
        </a>

    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Excercise-2 : Run Gradient Boosting Model")
