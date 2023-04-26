import streamlit as st
from st_pages import add_indentation
from PIL import Image
from streamlit_extras.switch_page_button import switch_page

lime = Image.open("./boosting/static/lime.JPG")

add_indentation()

st.header("Issues with approaches so far")

st.markdown("""

        **Impurity based feature engineering** and **Permutation based Feature engineering** both explain which feature is important for model performance.
        - They **don’t** explicitly explain **which feature played a more important role in predicting a particular instance**.



        For that, we can use techniques like **LIME and SHAP**.

        Let’s look into how LIME does it.

        ___

        #### LIME

        In order to get interpretability of which feature played important role for a particular instance:
        - It generates set of similar instances (perturbations by adding noise or sampling from distribution) i.e. small variations of given instance
        - It then uses the model to predict output of these generated instances
        - It then fit easily interpretable model (Log reg, DT) those these generated instances and their predicted output
        - Using this interpretable model, it can easily identify features which contribute the most for predicting this instance.


        <a href = "https://lime-ml.readthedocs.io/en/latest/lime.html#module-lime.lime_tabular">LIME documentation</a>

        Let's look into its code:

        ----

     """, unsafe_allow_html=True)

st.markdown("#### Installing and Package importing")

code = """
 !pip install lime

 from lime.lime_tabular import LimeTabularExplainer


     """

st.code(code, 'python',  line_numbers=True)

st.markdown("#### Defining LIME explainer object")

code = """
 predict_fn = lambda x: gbdt.predict_proba(x)

# Defining the LIME explainer object
explainer = LimeTabularExplainer(X_train,
                                mode='classification',
                                class_names=['Did not Default', 'Default'],
                                 training_labels=y_train,
                                 feature_names=preprocessor.get_feature_names_out()
                                 )

     """

st.code(code, 'python',  line_numbers=True)

st.markdown("#### Get explanaition of an instance")

code = """
 # using LIME to get the explanations

exp=explainer.explain_instance(X_test[10,:], predict_fn,)
exp.show_in_notebook(show_table=True)

     """

st.code(code, 'python', line_numbers=True)

st.image(lime)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Challenges")
