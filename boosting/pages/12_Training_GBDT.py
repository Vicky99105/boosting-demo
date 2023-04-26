import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()

gbdt_score = Image.open("./boosting/static/gbdt_score.JPG")

st.header("Training GBDT")

st.markdown("""

    ---

    #### Exercise-2: Run Gradient Boosting model on data



    #### Hyperparam tuning:

""")


code = '''

from sklearn.model_selection import GridSearchCV

params = {"learning_rate": [0.1, 0.3],
          "n_estimators": [100, 200, 300],
          "min_samples_split": [2, 4, 8, 10],
          "max_depth": [1, 3, 5, 10]}

gbdt = GradientBoostingClassifier(verbose = 1)

clf = GridSearchCV(gbdt, params, scoring = 'f1', n_jobs = -1, cv = 3, verbose = 1, return_train_score = True)

clf.fit(X_train, y_train)

'''

st.code(code, language='python', line_numbers=True)


st.markdown("""

    ---

    #### Selecting best model

""")


code = '''

gbdt = GradientBoostingClassifier(**clf.best_params_)

gbdt.fit(X_train, y_train)

'''

st.code(code, language='python', line_numbers=True)

st.markdown("""

    ---

    #### Predict score

""")


code = '''

y_train_pred = gbdt.predict(X_train)
y_test_pred = gbdt.predict(X_test)

'''

st.code(code, language='python', line_numbers=True)


st.image(gbdt_score)

st.markdown("""

    ----
    #### Now that we have learnt about details of boosting, what do you think are Challenges with Boosting?


""")


options = [
    "Sensitive to outliers",
    "It overfits easily if not trained properly",
    "A lot of hyperparameters, tuning process is very tedious",
    "Difficult to interpret. ",

]

selected = st.multiselect("", options)

selected = ", ".join(selected)


if st.button('Submit'):
    st.markdown(f"""
        #### Your response:

        **{selected}**

        ---

        #### Your peers response:

        **Raghav**:  Sensitive to outliers, It overfits easily if not trained properly, A lot of hyperparameters, tuning process is very tedious

        **Vishal**: Sensitive to outliers, It overfits easily if not trained properly, A lot of hyperparameters, tuning process is very tedious

        ---

        #### Correct Answer:

        - Sensitive to outliers
        - It overfits easily if not trained properly
        - A lot of hyperparameters i.e tuning process is very tedious
        - Difficult to interpret.


        #### Explanation

        - If there are outliers in data, it’ll also fit to those outliers.
        - Take care of hyperparam such as the number of estimators, learning rate, max_depth etc as it can easily overfit.
        - As there are a lot of hyperparam involved, it is a tedious task to fine tune them.
        - In DT, where it is easy to visualize the splits of a given tree and see how the decision is being made for a given data point,
            - Since there are M trees involved here, it gets difficult to interpret.

    """, unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Optuna")
