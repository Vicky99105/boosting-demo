import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()


dt_score = Image.open('./static/dt_score.jpg')


st.header("Boosting - Another Meta Learning Algorithm")

st.markdown("""
    ---

    #### Excercise 1: Run Decision Tree on train data.

    **Results: Train f1-score - 0.8, Test f1-score - 0.78 → Low Variance**

""")


st.image(dt_score, )


st.markdown("""

    #### Would you apply Random Forest to improve the performance?

    > No, Random Forest typically solves the problem of high variance

    ---

    """)


st.markdown("####  What would you do to improve the model performance? Assume you can train as many Decision Trees as you want.")

answer = st.text_area(
    "Feel free to explore the resources on internet. Type out in text box below and Submit using Ctrl + Enter")

if(answer):

    st.markdown(f"""
        #### Your thoughts:
    """)
    st.write(answer)

    st.markdown(
        f"""



        #### Here's what your peers think:

        **Vishal**:

        - Increase the depth of DT

        **Vicky**

        - Can't make it complex, it'll overfit

        ---
    """
    )

    st.markdown("""
        #### Conclusion:

        Here's what we can do:

        - Check if **Decision Tree** can further be made more **complex**

            - We can make DT complex by **Increasing depth**, **# of leaves**, **branches**.


        - Train a **subsequent Decision Tree** only to only **improve the error of previous learner**


        Let's expore what's mentioned in point no. 2

    """)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Boosting Fundamentals")
