import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page


add_indentation()

missing = Image.open('./boosting/static/missing.JPG')

st.header("Handling Missing values")
st.markdown("---")


st.image(missing, caption="Missing value percentage", width=500)

st.markdown(
    """
        **During analysis, We saw that there are two columns with missing values.**


        - **loan_interest_rate** - ~10% missing data

        - **person_emp_length** - ~ 3% missing data

        #### How would you deal with this situation ?""")

options = ['Drop the rows with missing data',
           'Drop the columns with missing data',
           'Use Mean imputation',
           'Use Median imputation', ]

selected = st.radio(label="", options=options, )


if st.button('Submit', ):
    st.markdown(f"""
        ___

        #### Your response:

        **{selected}**

        ---

        #### Your peers response:

        **Raghav**:  Use Mean imputation

        **Gyan**: Use Median imputation

        ---

        #### Answer:

        **Use Median imputation**

        ___

        #### Conclusion:

        There are **two columns with missing percentage < 30%**.

        - **Loan interest rate** has missing value %age of 10%

        - While **person employment length** has missing value %age of 3%

        So, **instead of discarding** them, we’ll go forward with **imputation**.

        - Based on analysis so far, the **distributions are right skewed**.
            - It would be **unwise** to use **Mean imputation** as **mean** will get dragged due to skewness
            - Hence, We’ll use **median imputation**.


    """)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Correlation")
