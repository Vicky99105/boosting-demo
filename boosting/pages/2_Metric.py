import streamlit as st
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page


add_indentation()

st.markdown("#### What metric(s) would you optimize while building a PD classification model?")

options = ['Recall', 'F1 score', 'Precision', 'Accuracy', 'Log Loss']

selected = st.multiselect(label="", options=options)

selected = ", ".join(selected)

if st.button('Submit'):
    st.markdown(f"""
        #### Your response:

        **{selected}**

        ---

        #### Your peers response:

        **Raghav**:  F1 score

        **Anant**: Precision, Recall, F1 score

        ---

        #### Answer:

        **Precision, Recall, F1 score**

        #### Conclusion:

        A Good Classifier should
        - Minimize bad customer being predicted as good - **Low FN → High Recall**
        - Minimize good customer being predicted as bad - **Low FP → High Precision**

        Since we have to **optimize** for **both Recall and Precision**, we can optimize for **f1-score**.



    """)

else:
    st.info("Please select atleast one option. Feel free to select more than one :)")
    st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Dataset Exploration")
