import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page


add_indentation()

dataset_1 = Image.open('.boosting/static/dataset_1.jpg')
dataset_2 = Image.open('.boosting/static/dataset_2.jpg')

st.header("Dataset")

st.markdown("""

  ---

  **Let’s look into the dataset:**

  **Dataset <a href="https://drive.google.com/file/d/14jNI9sxp2lVMoKHjAWLPwPwBvaF0drJ1/view?usp=sharing">link</a>**


""", unsafe_allow_html=True)

st.info("Tip: Incase you want maximize the image, use fullscreen tool present on top right of image.")


st.image(dataset_1, caption='Dataset info - Features card and data.info() ')

st.image(dataset_2, caption='Dataset info - data.describe() ')

st.markdown("""

    **Total - 13 columns.**

    **Out of these 12, we’ll use loan_status as target variable.**

    #### Given the dataset info, what series of analysis would you apply on the given dataset ?

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

        - There are 13 columns.
        - Null values in 2 columns
        - Oldest customer is 94 yr old. while median age of customer is 26
        -

        **Vicky**
        - Total 13 columns in dataset
        - 8 numerical and 4 categorical

        ---
    """
    )

    st.markdown("""
        #### Conclusion:

        The **analysis** can include the following:

        - Are there any **missing values** in the dataset ?

        - Is the **data imbalanced**?

        - Is there any **multicollinearity** in data?

        - What’s the **association of features** with the **target variable**?

        - What is the **distribution of features**? Is the feature too skewed?  Are there outliers in data ?

        - How are **features correlated with the target variable** ?






    """)

else:
    st.info("Remember: Sharing is caring... :)")
    st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Analysing")
