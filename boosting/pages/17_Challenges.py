import streamlit as st
from st_pages import add_indentation

add_indentation()
st.header("Challenges")

tab_1, tab_2, tab_3 = st.tabs(["Challenge 1", "Challenge 2", "Challenge 3"])

with tab_1:
    st.markdown("""
        #### What are the reason for performing additive combinations in boosting ?


    """)

    options = ["For combining shallow trees",
               "For splitting shallow trees",
               "For decreasing bias",
               "For making model optimized by decreasing variance"]

    selected = st.multiselect(" ", options=options)

    # selected = ", ".join(selected)

    if st.button("Submit") and selected:

        st.markdown("""
        ---

         #### You selected: """)

        for option in selected:
            st.write(f"- {option} \n")

        st.markdown(f"""



            #### Correct Answer:

            - For combining shallow Trees
            - For decreasing bias

            #### Explanation:
            - In boosting, we have base learners which are of low variance and high bias i.e. shallow trees.
            - We do additive combination in which we combine these shallow trees to make the model complex.

        """)
    else:
        st.warning("Please select atleast one option :)")


with tab_2:
    st.markdown("""

        #### The biggest risk of GBDT is it easily gets overfit if we are not careful. How do we tackle this problem?

    """)

    options = ["Increase tree depth",
               "Increase the number of base learners",
               "Use learning rate hyperparam",
               "None of the above"]

    selected = st.radio(" ", options=options)

    # selected = ", ".join(selected)

    if st.button("Submit ") and selected:

        st.markdown(f"""
         ---

         #### You selected:

         - {selected}

         """)

        st.markdown(f"""

        #### Correct Answer:

        - Use learning rate hyperparam

        #### Explanation:
        - Learning rate acts as a regularization term and hence  helps in tacking overfiting
        - Its value lie between 0 and 1.
        - Intutively, it shrinks the impact of mth model so that models don't overfit easily.

        """)
    else:
        st.warning("Please select an option :)")


with tab_3:
    st.markdown("""

        #### Examine the following statements carefully and select the correct option:

        **Statement 1**: When comparing two models of GBDT with same validation accuracy, the model with larger max_depth
        is better; as boosting works best when the trees have more depth.

        **Statement 2**: The individual trees are all independent of each other in boosting as their aggregating together
        gives us the final statement.

    """)

    options = ["Only Statement 1 is correct",
               "Only Statement 2 is correct",
               "Both statements are correct",
               "Both statements are incorrect"]

    selected = st.radio(" ", options=options)

    # selected = ", ".join(selected)

    if st.button(" Submit ") and selected:

        st.markdown(f"""
         ---

         #### You selected:

         - {selected}

         """)

        st.markdown(f"""

        #### Correct Answer:

        - Both statements are **incorrect**

        #### Explanation:
        - **Statement 1 is incorrect** coz larger max_depth doesn't necessarily mean the model is better.
            - In fact, increasing the max_depth of the trees in as GBDT model may lead to overfitting and decreased generalization.
            - The best max_depth for a model depends on the complexity of the data and the specific characteristics of the model.

        - **Statement 2 is also incorrect**. While the individual trees in boosting are trained independently.
            - However, they are not completely independent of each other.
            - The predictions of each tree are used to update the weigths of the training instances in the next iteration.
            - So, trees are not completely independent.

            <br><br>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please select an option :)")

    _, col2, col3 = st.columns(3, gap='large')

    with col3:
        if st.button("Finish"):
            st.balloons()
