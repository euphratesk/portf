import streamlit as st
import numpy as np
import pandas as pd
import pickle
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Machine learning models


model_xgboost = pickle.load(open(r'C:\Users\Admin\OneDrive\Desktop\TECHPRO\AMZstreamlit\xg_best.pkl', 'rb'))
model_random_forest = pickle.load(open(r'C:\Users\Admin\OneDrive\Desktop\TECHPRO\AMZstreamlit\rf_best.pkl', 'rb'))


# Dictionary to map country abbreviations to full names
country_mapping = {
    'CA': 'Canada',
    'AE': 'United Arab Emirates',
    'SG': 'Singapore',
    'AU': 'Australia',
    'JP': 'Japan',
    'SA': 'Saudi Arabia',
    'MX': 'Mexico'
}

# Create input boxes for the given features in the sidebar
st.sidebar.header('Parameters')
total_account_count = st.sidebar.number_input("Total Account Count", min_value=0, step=1)
total_income = st.sidebar.number_input("Total Income", min_value=0.0, step=1.0)
total_product_count = st.sidebar.number_input("Total Product Count", min_value=0, step=1)
total_profit = st.sidebar.number_input("Total Profit", min_value=0.0, step=1.0)

# Create a multiselect dropdown for countries using full names in the sidebar
selected_countries = st.sidebar.multiselect("Select Countries", list(country_mapping.values()))
selected_c = [1 if country in selected_countries else 0 for country in country_mapping.values()]




# Input for registration date
register_date_input = st.sidebar.date_input("Enter Registration Date", datetime.now())

# Calculate active months
today = datetime.now()
active_months = relativedelta(today, register_date_input).months + relativedelta(today, register_date_input).years * 12

# Display the result
st.sidebar.write(f"Active Months: {active_months}")

# Create a multiselect dropdown for packages in the sidebar
package_options = ['Paket1 - 5000 e kadar', 'Paket2 - 10000 e kadar', 'Paket3 - 25000 e kadar',
                   'Paket4 - 50000 e kadar', 'Paket5 - 100000 e kadar', 'Paket8 - 150000 e kadar',
                   'Paket6 - 200000 e kadar', 'Paket9 - 250000 e kadar']

selected_package_option = st.sidebar.selectbox("Select a Package", package_options)

# Convert the selected option into a list
selected_package_index = package_options.index(selected_package_option)
selected_packages = selected_package_index
st.sidebar.write(selected_packages)


# Create radio buttons for registration source in the sidebar
registration_source_options = ['Diger', 'Amazon Camp', 'Sosyal Medya', 'Seminer', 'Arkadaş', 'Danışmanlık']

selected_registration_source = st.sidebar.radio("Select Registration Source", registration_source_options)
selected_registration_source = int(pd.Series(selected_registration_source).map({i:k for  i,k in zip(['Diger', 'Amazon Camp', 'Sosyal Medya', 'Seminer', 'Arkadaş', 'Danışmanlık'],[0,1,2,3,4,5])}).values[0])
st.sidebar.write(selected_registration_source)


# Model selection dropdown and descriptions
st.header('Select a Statistical Model')
model_options = {"Logistic Regression": model_logistic, "Random Forest": model_random_forest, "XGBoost": model_xgboost} 
selected_model_name = st.selectbox("Select Model", list(model_options.keys()))
selected_model = model_options[selected_model_name]

model_features = {
    'total_account_count': total_account_count,
    'total_income': total_income,
    'total_product_count': total_product_count,
    'total_profit': total_profit,
    'CA': selected_c[0],
    'AE': selected_c[1],
    'SG': selected_c[2],
    'AU': selected_c[3],
    'JP': selected_c[4],
    'SA': selected_c[5],
    'MX': selected_c[6],
    'active_months': active_months,
    'packages_encoded': selected_packages,
    'registration_source_encoded': selected_registration_source
}

# Convert the dictionary values into a list
features = list(model_features.values())
features = []
features.extend([total_account_count,total_income,total_product_count,total_profit])
features.extend(selected_c)
features.extend([active_months,selected_packages,selected_registration_source])

#features = np.array(features)






# Add a predict button in the main canvas
if st.button("Run Prediction"):
    # Scale the input values for the selected model
   

    # Dummy prediction for demonstration. Replace with your actual prediction logic.
    prediction = selected_model.predict([features])
    probability = selected_model.predict_proba([features])[0][1] * 100

    # Display the prediction result and probability in the main canvas
    st.title('Prediction Result')
    st.write(f"Predicted Outcome: {prediction[0]}")
    st.write(f"Probability : {probability:.2f}%")
