import os
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.cluster import KMeans
import pickle

# Load the daily CSV file into a DataFrame
base_dir = "/home/airflow/ml/clusters/prod/Daily_csv"
today = datetime.now().strftime('%b_%d_%Y')
daily_csv_path = f"{base_dir}/{today}.csv"

try:
    df = pd.read_csv(daily_csv_path)
    print("Daily CSV data loaded successfully.")
except FileNotFoundError:
    print(f"File not found: {daily_csv_path}")

# Define your features
continuous = ['bidirectional_bytes', 'bidirectional_cwr_packets', 'bidirectional_fin_packets',
              'bidirectional_get_request_bytes', 'bidirectional_l2_bytes', 'bidirectional_packets',
              'bidirectional_psh_packets', 'bidirectional_rst_packets', 'bidirectional_stddev_ps',
              'bidirectional_syn_packets', 'dns_query_len', 'dst2src_ack_packets', 'dst2src_cwr_packets',
              'dst2src_fin_packets', 'dst2src_get_request_bytes', 'dst2src_mean_ps', 'dst2src_syn_packets',
              'package_count', 'src2dst_bytes', 'src2dst_ack_packets', 'src2dst_cwr_packets',
              'src2dst_fin_packets', 'src2dst_get_request_bytes', 'time_to_live']
boolean = ['dns_query_has_sub_domain', 'login_fail_count']
nominal = ['direction', 'destination_port', 'dns_response_code', 'application_category_name',
           'request_type', 'status_code', 'source_port', 'tunnel_value', 'vlan_identifier']

# Process the data
dc = df[continuous].values
dn = df[nominal].values
db = df[boolean].values

# Create copies of the data for processing
dc1 = dc.copy()
dn1 = dn.copy()
db1 = db.copy()

# Scaling continuous features
scaler = MinMaxScaler()
dc = scaler.fit_transform(dc)

# Function to encode nominal features
def enfunc(nominal_data):
    if nominal_data.size == 0:
        raise ValueError("Input nominal data array is empty.")
    nominal_data = np.array(nominal_data, dtype=str) if len(nominal_data.shape) == 2 else np.array([nominal_data], dtype=str)
    nominal_data = np.where(np.isin(nominal_data, [None, '', 'nan', 'NaN', np.nan, np.inf, -np.inf]), 'Unknown', nominal_data)
    encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
    encoded_array = encoder.fit_transform(nominal_data)
    return encoder, encoded_array

# Encode nominal data
encoder, dn = enfunc(dn)

# Combine the data for training
trainset = np.concatenate((dn, dc, db), axis=1)

# Train the clustering model
model = KMeans(n_clusters=8, init="k-means++")
labels = model.fit_predict(trainset)

# Create a new folder in the daily_pickle volume
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')  # Use the current time as a timestamp
pickle_dir = f"/home/airflow/ml/clusters/prod/Daily_pickle/{timestamp}"
os.makedirs(pickle_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Save the scaler, encoder, and model to the new directory
with open(f"{pickle_dir}/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f, protocol=pickle.HIGHEST_PROTOCOL)

with open(f"{pickle_dir}/encoder.pkl", "wb") as f:
    pickle.dump(encoder, f, protocol=pickle.HIGHEST_PROTOCOL)

with open(f"{pickle_dir}/model.pkl", "wb") as f:
    pickle.dump(model, f, protocol=pickle.HIGHEST_PROTOCOL)

print("Pickle files saved successfully.")

