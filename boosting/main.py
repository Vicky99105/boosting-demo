import streamlit as st

from st_pages import add_page_title, show_pages_from_config
from streamlit_extras.switch_page_button import switch_page


add_page_title()  # By default this also adds indentation

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages_from_config()

st.markdown("""

    ---

    #### 1. Usecase: Credit risk modeling & its Importance

    #### 2. Role of ML in Risk modeling

    #### 3. Boosting

    #### 4. Automated Hyperparam tuning

    #### 5. Model interpretation


""")


col1, col2, col3 = st.columns(3)

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Importance of credit risk modeling")
