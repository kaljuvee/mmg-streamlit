# pages/3_Quote_Page.py
import streamlit as st
import pandas as pd
from utils import switch_page

def find_providers(specialty):
    # Read the CSV file
    df = pd.read_csv('providers.csv')
    
    # Filter based on selected specialty
    filtered_df = df[df['SubSpecialty'] == specialty]
    
    return filtered_df

st.image("img/mmg-logo-small.png", width=200)
st.title("My Medical Gateway")
st.subheader("Quote Page")

st.write("Here are the providers for your selected specialty:")

# Retrieve the selected specialty from session state
selected_specialty = st.session_state.get('selected_specialty', None)
first_name = st.session_state.get('first_name', 'Customer')

# Display a personalized message
st.write(f"Here is your quote, {first_name}!")

if selected_specialty:
    results = find_providers(selected_specialty)
    
    if results.empty:
        st.info("No providers found matching your criteria.")
    else:
        st.success(f"Found {len(results)} provider(s) matching your criteria.")
        
        for index, row in results.iterrows():
            with st.expander(f"Doctor: {row['Doctor']} - Clinic: {row['ClinicName']}"):
                st.write(f"**Clinic Name:** {row['ClinicName']}")
                st.write(f"**Address:** {row['Address']}")
                st.write(f"**City:** {row['City']}")
                st.write(f"**Country:** {row['Country']}")
                st.write(f"**Specialty:** {row['Specialty']}")
                st.write(f"**SubSpecialty:** {row['SubSpecialty']}")
                st.write(f"**Quote(EUR):** {row['Quote(EUR)']}")
                
                if st.button(f"View Details of {row['Doctor']}", key=f"details_{index}"):
                    switch_page("Clinic_Details")
else:
    st.warning("No specialty selected. Please go back and select a specialty.")

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