import pickle
import streamlit as st
import pandas as pd
import pathlib

# Load the model (ensure this is done before the prediction function)
with open('classifier.pkl', 'rb') as pickle_in:
    classifier = pickle.load(pickle_in)

# Define prediction function
def prediction(gender, max_bpm, avg_bpm, resting_bpm, fat_percentage, water_intake, bmi):
    # Pre-process the gender input (convert to 0 or 1)
    if gender == "Male":
        Gender = 0
    else:
        Gender = 1

    # Correct input format for prediction
    prediction_result = classifier.predict([[Gender, max_bpm, avg_bpm, resting_bpm, fat_percentage, water_intake, bmi]])

    return prediction_result

# Function to load CSS file
def load_css(file_path):
    try:
        with open(file_path, 'r') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("CSS file not found. Please check the file path.")

# Load the external CSS
css_path = pathlib.Path("style.css")
load_css(css_path)

# This is the main function in which we define our webpage
def main():
    # Front end elements of the web page
    html_temp = """
    <div style="padding: 13px;">
        <h1 class="title">Workout Type Classifier</h1>
    </div>
    """

    # Display the front-end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # Create columns for displaying images side by side
    col1, col2 = st.columns(2)

    with col1:
        st.image("yoga.jpg", width=300)  # Adjust the width as needed

    with col2:
        st.image("hiit.jpg", width=300)  # Adjust the width as needed

    # Create input boxes in which the user can enter data required to make a prediction
    gender = st.selectbox('Gender', ("Male", "Female"))

    # Add a thin grey line after the gender dropdown
    st.markdown("<hr>", unsafe_allow_html=True)

    # Create columns for the 3 heartbeat values
    col1, col2, col3 = st.columns(3)
    with col1:
        max_bpm = st.number_input('Max BPM', min_value=40, max_value=300, step=1)
    with col2:
        avg_bpm = st.number_input('Average BPM', min_value=40, max_value=300, step=1)
    with col3:
        resting_bpm = st.number_input('Resting BPM', min_value=40, max_value=300, step=1)

    # Add a grey line after the heart rate boxes
    st.markdown("<hr>", unsafe_allow_html=True)

    # Create columns for Fat Percentage and BMI using sliders
    col4, col5 = st.columns(2)
    with col4:
        fat_percentage = st.slider('Fat Percentage', min_value=0.0, max_value=100.0, step=0.1)
    with col5:
        bmi = st.slider('BMI', min_value=0.0, max_value=50.0, step=0.1)

    # Add a grey line after Fat Percentage and BMI
    st.markdown("<hr>", unsafe_allow_html=True)

    # Water intake number input
    water_intake = st.number_input('Water Intake (L)', min_value=0.0, max_value=10.0, step=0.1)

    # Add a grey line after Water Intake
    st.markdown("<hr>", unsafe_allow_html=True)

    # Classify button
    if st.button("Classify", help="Click to get your workout classification"):
        result = prediction(gender, max_bpm, avg_bpm, resting_bpm, fat_percentage, water_intake, bmi)
        st.success(f'Your classical workout is {result[0]}')
        print(result)

if __name__ == '__main__':
    main()
