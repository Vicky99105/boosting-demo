
import streamlit as st
from PIL import Image
from st_pages import add_indentation
from streamlit_extras.switch_page_button import switch_page

add_indentation()

optuna_score = Image.open("./static/optuna_score.jpg")

st.header("Automated Hyperparameter tuning using Optuna")


st.markdown("""

    As we saw while **training GBDT using Random/GridSearch**,
    - If we **increase** the combinations of **hyperparams** to try on, the **training becomes tedious**
    - As it’ll try every/random combination

    ---

    #### Is there any better strategy ?

    We can fine tune model using **Optuna**
    - It provides various **sampling strategies** for selecting hyperparam.
        - In simple terms, it doesn’t try out all the combinations blindly
        - It **remembers (historical trails)** what hyperparam worked and tries the next combination based on that.
        - It has various **pruning strategies** which stops training for unpromising hyperparam early on.

        Hence, reducing the time for fine tuning the model.

    ---

    #### Let’s do the hyperparam tuning using Optuna


""")


code = '''
# Step 1 : Define objective
def objective(trial):

  # Step 2. Setup values for the hyperparameters:
    max_depth = trial.suggest_int('max_depth', 1, 15)
    n_estimators = trial.suggest_int('n_estimators', 50, 500)
    learning_rate = trial.suggest_float('learning_rate', 0.1, 0.5)
    min_samples_split = trial.suggest_int('min_samples_split', 2, 20)
    min_samples_leaf = trial.suggest_int('min_samples_leaf', 2, 20)
    subsample = trial.suggest_float('subsample', 0.6, 1)
    criterion = trial.suggest_categorical('criterion', ['friedman_mse', 'squared_error'])
    # ccp_alpha = trial.suggest_float('ccp_alpha', 0, 0.5)
    model = GradientBoostingClassifier(n_estimators = n_estimators,
                                         max_depth=max_depth,
                                         learning_rate = learning_rate,
                                         criterion = criterion,
                                         min_samples_split=min_samples_split,
                                         min_samples_leaf=min_samples_leaf,
                                         # ccp_alpha = ccp_alpha
                                         )

    # Step 3: Scoring method:
    score = cross_val_score(model, X_train,y_train, n_jobs=-1, cv=3, scoring = 'f1')
    mean_score = score.mean()
    return mean_score

'''

st.code(code, language='python',  line_numbers=True)


st.markdown("#### Maximize/Minimize the objective")

code = """
# Step 4: Running it
study = optuna.create_study(direction="maximize", study_name = 'GBDT')
study.optimize(objective, n_trials=100, n_jobs = -1)

"""

st.code(code, 'python', line_numbers=True)

st.markdown("""
---

#### Get best params

""")


code = '''

print(f"Best score : {study.best_value}")
print (f"Best params: {study.best_params}")


gbdt = GradientBoostingClassifier(**study.best_params)

gbdt.fit(X_train, y_train)

'''

st.code(code, language='python', line_numbers=True)


st.image(optuna_score)


st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col3:
    switch_button = st.button("Mark as Complete")
    if switch_button:
        switch_page("Feature Importance using sklearn")
