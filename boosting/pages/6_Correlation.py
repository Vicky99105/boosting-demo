
import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()

corr = Image.open('./boosting/static/correlation.png')


st.header("Are features correlated with the target variable ?")


tab1, tab2 = st.tabs(["Code Up", "Interesting correlations"])

with tab1:
    st.markdown("""
        ##### CODE: Can you write up code to display a heatmap of correlation matrix (spearman) for only numerical / boolean features ?
        Reference: <a href="https://seaborn.pydata.org/generated/seaborn.heatmap.html">Heatmap</a>,
                    <a href = "https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html">correlation</a>
    """, unsafe_allow_html=True)

    answer = st.text_area("Take your time in exploring the links above before attempting.")

    code = '''plt.figure(figsize=(8,8))
    sns.heatmap(df.corr(method = 'spearman', numeric_only = True), cmap='Blues', annot=True, fmt='.2f')
    plt.show()
    '''

    if st.button("Submit") and answer:

        st.write("Let's evaluate the solution now")

        st.markdown("#### Solution:")
        st.code(code, language='python', line_numbers=True)

        st.image(corr, caption="Correlation heatmap", width=600)

        st.markdown("""
            **Here are some interesting insights from the correlation matrix:**

            - Both **Loan interest rate** and **loan percent income** are **positively correlated** with **loan status**

                - i.e. as value of interest rate/ loan percent income increase, value of loan status also increases (i.e. 1 -> defaults)

            - There is a **negative correlation** between **loan status** and a **person's income**.

                - As a person's income increases, loan status decreases i.e. less likely to default.

        """)

with tab2:
    st.markdown("""


        #### What other interesting correlations can you find from this ?
    """)

    answer = st.text_area("")

    st.write(answer)

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

            - No other insights

            **Vicky**

            - Person's age is highly correlated with credit history length

            ---
        """
        )

    st.markdown("""



        #### What’s next?

        Fit the model!

        **But, we need to encode the data first.**


    """)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="large")

    with col3:
        switch_button = st.button("Mark as Complete")
        if switch_button:
            switch_page("Encoding")
