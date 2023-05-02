import streamlit as st
import pickle
import pandas as pd
from model import output






st.title("Welcome to flower prediction app")

a = float(st.number_input("sepal length in cm"))
b = float(st.number_input("sepal width in cm"))
c = float(st.number_input("petal length in cm"))
d = float(st.number_input("petal width in cm"))

btn = st.button("predict")

if btn:
    pred = output(a, b, c, d)
    outp = pred[0]
    if outp == 0:
        st.write("Iris-setosa")
        st.image('setosa.jpg')
    elif outp == 1:
        st.write("Iris-versicolor")
        st.image('versicolor.jpg')
    else:
        st.write("Iris-virginica")
        st.image('verginca.jpg')
      

