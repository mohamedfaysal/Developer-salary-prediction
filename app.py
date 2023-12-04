import streamlit as st
from predict_page import *
from explore_page import *


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

country = st.selectbox("Country", countries)
education = st.selectbox("Education Level", education)

experience = st.slider("Years of Experience", 0, 50, 3)

ok = st.button("Calculate Salary")

if ok :
    X = np.array([[country, education, experience]])
    X[:, 0] = le_country.transform(X[:,0])
    X[:, 1] = le_education.transform(X[:,1])
    X = X.astype(float)

    salary = regressor.predict(X)
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")
