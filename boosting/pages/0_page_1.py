import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page


add_indentation()

crisis = Image.open("./boosting/static/crisis.jpg")

st.header('Importance of credit risk modeling')

st.write("---")

st.image(crisis, width=500)

tab1, tab2 = st.tabs(["Discussion-1",
                      "Discussion-2"])

with tab1:
    # question 1
    st.markdown("#### Do you know how the 2008 recession was related to credit risk modeling? If so why ? ")

    answer = st.text_input(" ", placeholder="Type your thoughts here...")

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

            - No

            **Vicky**

            - banks failed.

            ---
        """
        )

        st.markdown("""

            #### Conclusion:

            Banks provided mortgage home loans to low creditworthy customers""")
    else:
        st.info("Share your thoughts to see what's your peers take on the question. :)")

with tab2:
    # question 2

    st.markdown("#### But why would banks provide loans to risky borrowers?")

    answer = st.text_input(" ", placeholder="Type your thoughts here.....")

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

            - To get more revenue

            **Vicky**

            - Risky loans come with higher interest rate. Hence, more income

            ---
        """
        )

        st.markdown("""

        #### Conclusion:

        - In case of default, outstanding amounts be recovered by seizing and selling the asset, thus banks assessed them as less risky lending

        - To compensate for the risk, banks instead charged higher interest rate and lend to masses""")

        st.markdown("""
        #### To Summarize:

        Credit risk modeling involves creating Business strategies at two levels
        1. **Minimize the risk of defaults** - provide loan or not
        2. **Maximize the earned interest** - adjust interest rate for risky customers
        3. **Maximize the recovery**, in case of default - by selling borrower’s assets

        <br> <br>

        """, unsafe_allow_html=True)

    else:
        st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col3:
        switch_button = st.button("Mark as Complete")
        if switch_button:
            switch_page("Role of ML")
