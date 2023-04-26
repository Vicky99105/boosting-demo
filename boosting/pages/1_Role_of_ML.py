import streamlit as st
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page


add_indentation()


st.header("Role of ML in risk modeling")

st.markdown("""
---

First step of credit risk modeling involves calculating the **Probability of Default (PD)**
""")


st.markdown("#### What do you think are the most relevant factors/features for predicting whether a person will default or not?")
answer = st.text_area(label=' ', value='',
                      placeholder="Type your thoughts here... and press Ctrl + Enter")

if(answer):

    st.markdown("""

            #### **Your thoughts:**
    """)

    st.write(answer)

    st.markdown(
        f"""

        ---

        #### Here's what your peers think:

        **Vishal**:

        - Age, Income, Employment Status, CIBIL score

        **Vicky**

        - CIBIL score, Income, Assets

        ---
    """
    )

    st.markdown("""
        #### **These factors can be**

        - **Income of person** - If a person earns more, he’s more likely to pay back

        - **Debt to income ratio** - What %age of income is a person asking for a loan?

        - **Employment history:** how long has the person been employed

        - **Loan history** : Are there any ongoing loans?

        - **Family dependents**: More dependents means less savings

        - **Age**: older person is more likely to have more assets/ savings

        - **CIBIL score:** higher the score, better the financial credibility

        - **Assets owned**: More the assets, more reliable is loan recovery in case of non payment

        - **Education qualification**: better education, better job. More reliable the customer.




    """)

else:
    st.info("Sharing is caring. Feel free to share what you feel. There's no right or wrong. Only thoughts. Deep thoughts... :)")
    st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Metrics")
