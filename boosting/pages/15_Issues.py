import streamlit as st
from st_pages import add_indentation
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

permutation_plot = Image.open("./static/permutation_plot.png")

add_indentation()

st.header("Issues with sklearn interpretation?")

st.markdown("""

    #### What do you think are the issues with impurity based feature importance ?

    Tree based model uses impurity based feature importance (i.e. reduction in impurity)

    """)

answer = st.text_area("Type your thoughts and press Ctrl + Enter to submit.")

if(answer):
    st.markdown("""

        There are two major issues with this
        - The feature importances are **calculated based on training data**, not on the predictions of test data.
        - They **favor high cardinality features**
            - As using high cardinality features for splitting provides more homogeneous nodes.


        ---

        #### How shall we deal with this issue ?

        We can use **Permutation based feature importance**

        - In this approach, we shuffle the values of a given feature and calculate the drop in model performance
        - If there is a significant drop, it means the feature is important.

        ----

    """)

    st.markdown("""
    #### Calculating Feature Importance using PFI

    sklearn documentation for <a href = "https://scikit-learn.org/stable/modules/generated/sklearn.inspection.permutation_importance.html">
    Permutation based Feature engineering
    </a>
    """, unsafe_allow_html=True)

    code = """

    from sklearn.inspection import permutation_importance

    result = permutation_importance(gbdt, X_test, y_test,
                               n_repeats=30,
                               random_state=0,
                               scoring = 'f1',
                               n_jobs = -1 )

        """

    st.code(code, 'python', line_numbers=True)

    st.markdown("##### Plotting the feature importances")
    code = """

    sorted_importances_idx = result.importances_mean.argsort()

    importances = pd.DataFrame(
        result.importances[sorted_importances_idx].T,
        columns=feature_names[sorted_importances_idx],
    )

    ax = importances.plot.box(vert=False, whis=10)
    ax.set_title("Permutation Importances (test set)")
    ax.axvline(x=0, color="k", linestyle="--")
    ax.set_xlabel("Decrease in F1 score")
    ax.figure.tight_layout()

        """

    st.code(code, 'python',  line_numbers=True)

    st.image(permutation_plot)

    st.markdown("""

            In case you want to read more permutation based Feature importance it,
            here's
            <a href = "https://www.scikit-learn.org/stable/auto_examples/inspection/plot_permutation_importance.html">sklearn blog</a>
            for it
            """, unsafe_allow_html=True)

    st.markdown("""

            ---

            #### Pros and Cons

            Pros:
            - Deals with both the flaws i.e. Feature Imp. on test dataset as well as no biases towards high cardinality features

            Cons:
            - It involves multiple permutations over a feature to find mean and std dev in loss of performance. Hence, it is a bit of a slow process.

            ---
        """)

else:
    st.info("Hurry! Your peers are waiting to read your thoughts! :)")

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Issues with approach")
