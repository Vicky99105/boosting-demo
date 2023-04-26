import streamlit as st
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()

st.header("Any existing model we can choose from ? ")

options = ['Logistic Regression', 'K-NN', 'Decision Tree']

st.markdown("""
    ---

    #### POLL: Out of classification models learnt so far, which model would you choose to solve this problem?

    """)
selected = st.multiselect("", options, )


selected = ", ".join(selected)

if st.button('Submit'):
    st.markdown(f"""
        #### Your response:

        {selected}

        ---

        #### Poll Count

         **Decision Tree - 2**

         **Logistic Regression - 1**

         **Knn - 0**

         **Decision Tree, Logistic Regression - 2**



        ---

        #### Let's discuss key points for each algo:

        **Logistic Regression**

        - It works well in high dimensionality space

        - May not be able to capture non linearity of data present

        **K-NN**

        - As banks operate on data scale of million of rows,

        - K-NN might fail here as inference time may go up.


        **Decision Tree**

        - Works well with combination of categorical and numerical data

        - Can capture non linearity of data using non linearity decision boundary


    """)

else:
    st.info("Please select atleast one option. Feel free to select more than one :)")
    st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Boosting Intro")
