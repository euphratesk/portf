import streamlit as st
import numpy as np
import pandas as pd
import pickle
from datetime import datetime
from dateutil.relativedelta import relativedelta
import seaborn as sns
import matplotlib.pyplot as plt

def set_bg_color():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-color: #FFD700;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_color()


df=pd.read_csv('df.csv')
# Machine learning models
#scaler= pickle.load(open(r'C:\Users\Admin\OneDrive\Desktop\TECHPRO\AMZstreamlit\scaler.pkl', 'rb'))
#model_logistic = pickle.load(open(r'C:\Users\Admin\OneDrive\Desktop\TECHPRO\AMZstreamlit\lg.pkl', 'rb'))
#model_xgboost = pickle.load(open(r'C:\Users\Admin\OneDrive\Desktop\TECHPRO\AMZstreamlit\xgb.pkl', 'rb'))
model_random_forest = pickle.load(open(r'C:\Users\Admin\OneDrive\Desktop\TECHPRO\Git-Github\AMZ\Churn\rf_best.pkl', 'rb'))


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
what_select =  package_options[selected_package_index]
st.sidebar.write('Selected package is: ', what_select)


# Create radio buttons for registration source in the sidebar
registration_source_options = ['Diger', 'Amazon Camp', 'Sosyal Medya', 'Seminer', 'Arkadaş', 'Danışmanlık']

selected_registration_source = st.sidebar.radio("Select Registration Source", registration_source_options)
selected_registration_source = int(pd.Series(selected_registration_source).map({i:k for  i,k in zip(['Diger', 'Amazon Camp', 'Sosyal Medya', 'Seminer', 'Arkadaş', 'Danışmanlık'],[0,1,2,3,4,5])}).values[0])
#st.sidebar.write(selected_registration_source)


# Model selection dropdown and descriptions
st.header('Select a Statistical Model')
model_options = {"Random Forest": model_random_forest} 
#"Logistic Regression": model_logistic, "Random Forest": model_random_forest, "XGBoost": model_xgboost
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

#features[[0,1,2,3,-3]] = scaler.transform([features[[0,1,2,3,-3]]])[0]


if st.button("Run Prediction"):
    # Scale the input values for the selected model

    # Dummy prediction for demonstration. Replace with your actual prediction logic.
    prediction = selected_model.predict([features])
    probability = selected_model.predict_proba([features])[0][1] * 100
    
    st.write(f"General Probability  : {probability:.2f}%")

    if prediction[0] == 1:
        if probability >= 66.6:
            # Include Font Awesome CSS
            st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)

            # Display caution icon with text
            st.markdown('<i class="fa fa-exclamation-triangle" style="color:red; "></i> **More likely to leave**', unsafe_allow_html=True)
            st.write(f"Prediction : Leave")
            st.write(f"Churn Rate : {probability:.2f}%")

        elif 50 < probability < 66.6:
            
            st.markdown("""
    <div style="display: flex; align-items: flex-start; justify-content: space-between; flex-direction: row; width: 100%;">
        <div style="flex-basis: 20%; display: flex; align-items: center; flex-direction: column;">
            <img src="https://cdn-icons-png.flaticon.com/512/3782/3782758.png" alt="icon" style="width: 150px; margin-bottom: 20px;">
        </div>
        <div style="flex-basis: 100%; display: flex; align-items: center; flex-direction: column;">
            <span style="text-align: center;">You can prevent this customer from leaving</span>
            <span style="text-align: center;">Look at parameters that effect this result </span>
        </div>
    </div>
""", unsafe_allow_html=True)
            
            st.write(f"Prediction : Leave")
            st.write(f"Churn Rate : {probability:.2f}%")
            
            # Include Font Awesome CSS
            st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)

            # Display caution icon with text
           

            

            # Display feature importance table for random forest model
            #st.write("Feature Importance Table for Random Forest Model:")
            rf_feature_imp = pd.DataFrame(data = model_random_forest.feature_importances_ ,index = model_features.keys()).sort_values(by = 0, ascending = False).rename({0:'Importance of parameters'},axis=1)
            #st.write(rf_feature_imp)  # Use 'rf_feature_imp' instead of 'feature_importance_table'
            fig = plt.figure(figsize=(20,10))
            plt.subplot(1, 2, 2)
            ax1 = sns.barplot(x=rf_feature_imp["Importance of parameters"], y=rf_feature_imp.index)
            
            ax1.set_title("Feature importance on the outcomes '\n' according to Random Forest", fontsize=22)
            ax1.tick_params(axis='x', labelsize=14)  # Set x-axis tick label font size
            ax1.tick_params(axis='y', labelsize=14)
            #ax1.set_xlabel(labelsize=14)
            for index, value in enumerate(rf_feature_imp["Importance of parameters"]):
                ax1.text(value, index, f'{value:.2f}', ha='left', va='center', fontsize=20)
            plt.show()    
                
            plt.subplot(1, 2, 1)    
            #correlation_matrix = X.corr()
           
                         
            #correlation_matrix = X.corr()
            correlation_matrix = df.corr()[["status_code"]].drop("status_code",axis=0).sort_values(by="status_code", ascending=False)

            # Plotting using Seaborn
            ax2 = sns.barplot(data=correlation_matrix, x="status_code", y=correlation_matrix.index,order = list(rf_feature_imp.index))
            for index, value in enumerate(correlation_matrix["status_code"]):
                ax2.text(value, index, f'{value:.2f}', ha='right', va='center', fontsize=20)
            ax2.set_title("Correlation Matrix & '\n' Direction of the Feature Importance", fontsize=24)
            ax2.tick_params(axis='x', labelsize=14)  # Set x-axis tick label font size
            ax2.tick_params(axis='y', labelsize=14) 
          


            plt.show()
            # Display the subplots
            plt.tight_layout()
            st.pyplot(fig) 


    


             
            
           


    elif prediction[0] == 0:
        if 33.3 <= probability < 50:
            st.markdown("""
    <div style="display: flex; align-items: flex-start; justify-content: space-between; flex-direction: row; width: 100%;">
        <div style="flex-basis: 20%; display: flex; align-items: center; flex-direction: column;">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLKPye3Wa_zJIc7JV91PLVjMnWkq0a1G06aw&usqp=CAU" alt="icon" style="width: 50px; margin-bottom: 20px;">
        </div>
        <div style="flex-basis: 100%; display: flex; align-items: center; flex-direction: column;">
            <span style="text-align: center;">Customer looks to stay but close to risky limit </span>
            <span style="text-align: center;">Draw a new strategy take a look what parameter effect result</span>
        </div>
    </div>
""", unsafe_allow_html=True)
            
    
            
            # Include Font Awesome CSS
            st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
            
            st.write(f"Prediction : Stay")
            st.write(f"Probability of keeping package is : {(100-probability):.2f}%")

            # Display caution icon with text
           

            

            # Display feature importance table for random forest model
            #st.write("Feature Importance Table for Random Forest Model:")
            rf_feature_imp = pd.DataFrame(data = model_random_forest.feature_importances_ ,index = model_features.keys()).sort_values(by = 0, ascending = False).rename({0:'Importance of parameters'},axis=1)
            #st.write(rf_feature_imp)  # Use 'rf_feature_imp' instead of 'feature_importance_table'
            fig = plt.figure(figsize=(20,10))
            plt.subplot(1, 2, 2)
            ax1 = sns.barplot(x=rf_feature_imp["Importance of parameters"], y=rf_feature_imp.index)
            
            ax1.set_title("Feature Importance on the outcomes '\n' according to Random Forest", fontsize=24)
            ax1.tick_params(axis='x', labelsize=14)  # Set x-axis tick label font size
            ax1.tick_params(axis='y', labelsize=20) 
            for index, value in enumerate(rf_feature_imp["Importance of parameters"]):
                ax1.text(value, index, f'{value:.2f}', ha='left', va='center', fontsize=20)
            plt.show()    
                
            plt.subplot(1, 2, 1)    
            #correlation_matrix = X.corr()
            correlation_matrix = df.corr()[["status_code"]].drop("status_code",axis=0).sort_values(by="status_code", ascending=False)

            # Plotting using Seaborn
            ax2 = sns.barplot(data=correlation_matrix, x="status_code", y=correlation_matrix.index,order = list(rf_feature_imp.index) )
            for index, value in enumerate(correlation_matrix["status_code"]):
                ax2.text(value, index, f'{value:.2f}', ha='right', va='center', fontsize=20)
            ax2.set_title("Correlation Matrix & '\n' Direction of the  Feature Importance", fontsize=24)
            ax2.tick_params(axis='x', labelsize=14)  # Set x-axis tick label font size
            ax2.tick_params(axis='y', labelsize=20) 
            

            plt.show()
            # Display the subplots
            plt.tight_layout()
            st.pyplot(fig) 

        elif probability < 33.3:
            
           

            # Display caution icon with text
            st.markdown('<i class="fa fa-check-circle" style="color:green; font-size:48px;"></i> **More likely to stay**', unsafe_allow_html=True)

# Display the larger icon
            st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">', unsafe_allow_html=True)
            
            
           

            #
            st.write(f"Prediction : Stay")
            st.write(f"Probability of keeping OneAMZ package is : {(100 - probability):.2f}%")
            








