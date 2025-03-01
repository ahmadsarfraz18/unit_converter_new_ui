import streamlit as st  

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .stApp {
            background-color: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .result-box {
            background-color: #4CAF50;
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
        }
        .convert-btn {
            background-color: #007BFF;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            width: 100%;
            cursor: pointer;
            border: none;
        }
        .convert-btn:hover {
            background-color: #0056b3;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #333;'>🌍 Simple Unit Converter 🔄</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Easily convert between different units of measurement</p>", unsafe_allow_html=True)

# Sidebar UI
st.sidebar.header("🔧 Select Conversion")
from_unit = st.sidebar.selectbox("From", ["meters", "kilometers", "miles", "centimeters", "feet"])
to_unit = st.sidebar.selectbox("To", ["meters", "kilometers", "miles", "centimeters", "feet"])
values = st.sidebar.number_input("Enter your value", min_value=0.0, format="%.2f")

# Conversion function
def Convert_units(values, from_unit, to_unit):
    conversion_formula = {
        "meters": {"kilometers": 0.001, "centimeters": 100, "feet": 3.28084},
        "kilometers": {"meters": 1000, "miles": 0.621371},
        "miles": {"kilometers": 1.60934, "meters": 1609.34},
        "feet": {"meters": 0.3048, "centimeters": 30.48},
        "centimeters": {"meters": 0.01, "feet": 0.0328084},
    }
    if from_unit == to_unit:
        return values
    factor = conversion_formula.get(from_unit, {}).get(to_unit, None)
    if factor is None:
        return None  
    return values * factor

# Conversion Button
if st.sidebar.button("Convert", key="convert_button"):
    result = Convert_units(values, from_unit, to_unit)
    if result is not None:
        st.markdown(f"<div class='result-box'>{values} {from_unit} is equal to <strong>{result:.3f} {to_unit}</strong></div>", unsafe_allow_html=True)
    else:
        st.error("Conversion not possible between selected units!")
