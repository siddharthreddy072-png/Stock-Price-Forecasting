import streamlit as st
import joblib

# Load the trained model
model = joblib.load("models/house_price_model.pkl")

# Application title
st.title("🏠 House Price Prediction")

st.write("Enter the house details to predict its price.")

# User inputs
area = st.number_input(
    "Area (sq.ft)",
    min_value=100,
    value=1200
)

bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    value=2
)

bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    value=2
)

stories = st.number_input(
    "Number of Stories",
    min_value=1,
    value=1
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    value=1
)

# Prediction button
if st.button("Predict Price"):

    # Prepare input data
    input_data = [[
        area,
        bedrooms,
        bathrooms,
        stories,
        parking
    ]]

    # Predict house price
    prediction = model.predict(input_data)

    # Display result
    st.success(
        f"Estimated House Price: ₹{prediction[0]:,.2f}"
    )
