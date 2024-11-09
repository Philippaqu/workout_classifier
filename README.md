# Workout Type Classifier App

## Overview
The **Workout Type Classifier** is a simple machine learning-based app built with Streamlit. It allows users to input various personal health data to predict their workout type. Based on the provided information, the app classifies the workout into one of two categories:
- **Yoga**
- **HIIT** (High-Intensity Interval Training)


## Features
- Classifies workout type into **Yoga** or **HIIT** based on inputs.
- Requires the following inputs from the user:
  - **Gender**
  - **Max BPM** (Maximum Heart Rate)
  - **Resting BPM** (Resting Heart Rate)
  - **Average BPM** (Average Heart Rate during exercise)
  - **BMI** (Body Mass Index)
  - **Water Intake** (in Liters)
  - **Fat Percentage** (percentage of body fat)
- Outputs the predicted workout type.

## How to Use

1. **Input your details**:
   - **Gender**: Choose between "Male" and "Female".
   - **Max BPM**: Enter your maximum heart rate (typically during intense activity).
   - **Resting BPM**: Enter your resting heart rate (usually measured in the morning).
   - **Avg BPM**: Enter your average heart rate during exercise.
   - **BMI**: Enter your Body Mass Index (can be calculated using weight and height).
   - **Water Intake**: Input how many liters of water you consume daily.
   - **Fat Percentage**: Enter your body fat percentage.
   
2. **Click "Predict"** to get your workout type.

3. **Results**:
   - The app will classify your workout type based on the inputs and display either **Yoga** or **HIIT** as the predicted workout type.

