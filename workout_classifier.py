import pickle
import streamlit as st
import pandas as pd


def prediction(gender, max_bpm, avg_bpm, resting_bpm, fat_percentage, water_intake, bmi):
    # Pre-processing user input
    if gender == "Male":
        gender = 0
    else:
        gender = 1

    # Making predictions
    prediction_result = classifier.predict([gender, max_bpm, avg_bpm, resting_bpm, fat_percentage, water_intake, bmi])

    # Return prediction result
    return prediction_result


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1>
    </div>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    # Following lines create input boxes in which the user can enter data required to make a prediction
    gender = st.selectbox('Gender', ("Male", "Female"))
    max_bpm = st.number_input('Max BPM', min_value=0, max_value=300, step=1)  # Assuming max bpm is a numeric input
    avg_bpm = st.number_input('Average BPM', min_value=0, max_value=300, step=1)
    resting_bpm = st.number_input('Resting BPM', min_value=0, max_value=300, step=1)
    fat_percentage = st.number_input('Fat Percentage', min_value=0.0, max_value=100.0, step=0.1)
    water_intake = st.number_input('Water Intake (L)', min_value=0.0, max_value=10.0, step=0.1)
    bmi = st.number_input('BMI', min_value=0.0, max_value=50.0, step=0.5)

    # When 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
      result = prediction(gender, max_bpm, avg_bpm, resting_bpm, fat_percentage, water_intake, bmi)
      st.success('Your classical workout is {}'.format(result[0]))  # Assuming the result is a list/array, access the first value
      print(result)  # You can print the result to the console if needed for debugging


if __name__=='__main__':
    main()
