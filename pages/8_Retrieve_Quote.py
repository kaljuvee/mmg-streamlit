# pages/Quote_Page.py
import streamlit as st
import pandas as pd
from utils import switch_page

# Dummy data for the providers
data = {
    "ClinicName": ["Ortho Center"],
    "Address": ["123 Main St"],
    "City": ["Riga"],
    "Country": ["Latvia"],
    "Specialty": ["Orthopedics"],
    "SubSpecialty": ["Arthroscopy"],
    "Quote (EUR)": ["500"]
}

# Create a DataFrame
df = pd.DataFrame(data)

st.image("img/mmg-logo-small.png", width=200)
# Streamlit app
st.title("My Medical Gateway")
st.subheader("Your Account")

# Display patient name if available in session state
first_name = st.session_state.get('first_name', '')
st.write(f"Here is your quote, {first_name}!")

st.write("Here are the providers for your selected specialty:")

# Display the DataFrame
st.dataframe(df)

# Navigation buttons
if st.button('Proceed to Payment'):
    switch_page("Payment")

if st.button('Back'):
    switch_page("Patient")

# Adding disclaimer text
st.write("""
<div class="disclaimer">
    <p>Our Confidentiality Undertaking & Standard Terms and our Fraud Prevention Policy are available for you to read. 
    We would like to draw your attention to them if this is your first contact with MMG and the MMG website.</p>
    <p>Mystery shopping from this website is not permitted. For full details, please refer to our Standard Terms above.</p>
    <p>My Medical Gateway International Limited (Company no. 1234567) is Registered in RAK IIC at Registered Office
    address G03 Emaar Building 3, Emaar Business Park, Dubai, UAE.</p>
</div>

""", unsafe_allow_html=True)
