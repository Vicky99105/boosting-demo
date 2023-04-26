import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page


add_indentation()

analysis_1 = Image.open('./static/analysis_1.jpg')
analysis_2 = Image.open('./static/analysis_2.png')
analysis_3 = Image.open('./static/analysis_3.png')
analysis_4 = Image.open('./static/analysis_4.png')


st.header("Analysing the data")

st.markdown("---")

st.markdown("##### Let’s perform some analysis based on the points mentioned")

st.info("Tip: Maximize the image by using fullscreen tool present at top right of each image.")

st.image(analysis_1, caption='')

st.image(analysis_2, caption='Data distribution of numerical features')

st.image(analysis_3, caption='Bivariate analysis of numerical features w.r.t loan_status')

st.image(analysis_4, caption='Bivariate analysis of catgeorical features w.r.t loan_status')


st.markdown("""

    #### What insights / inferences can you make out from the analysis above ?

""")


answer = st.text_area(label='', value='',
                      placeholder="Type your thoughts here... and press Ctrl + Enter")

if(answer):

    st.markdown(f"""
        #### Your thoughts:
    """)
    st.write(answer)

    st.markdown(
        f"""



        ---

        #### Here's what your peers think:

        **Vishal**:

        - There's missing values in dataset
        - Imbalanced class
        - Distribution is not normal

        **Vicky**

        -  There's missing values in dataset
        - Loan interest rate is higher for defaulted loans
        - loan percent income is higher for defualted loans

        ---
    """
    )

    st.markdown("""
        #### Conclusion:

        We can get the following **insights** from the plots above:

        - There are two columns with **missing values** i.e. **loan interest rate** and **person employment length**

        - Data set is **imbalanced** with **majority** of data belonging to **non default****  i.e class 0

        - **Distribution** of all numerical features are **right skewed**.

        - Majority of people who are applying for a loan don’t own a home. They are either living on rent or mortgage.

        - There is a small distinction between loan status when we look at medians of loan status and loan percent income

            - Higher loan interest are more likely to default

            - Higher loan percent income are more likely to default.


    """)

else:
    st.info("Hurry! Your peers are waiting for your opinion :)")
    st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Handling missing values")
