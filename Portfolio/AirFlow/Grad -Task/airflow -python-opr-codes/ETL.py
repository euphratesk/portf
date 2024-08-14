import csv
import os
import tarfile
from datetime import timedelta


from airflow import DAG
from airflow.operators.python_opereator import PythonOperator 
from airflow.utils.dates import days_ago


import pandas as pd 













default_args = {
    'owner' : 'my name',
    'start_date' : days_ago(0),
    'email' : ['me@gmai.com'],
    'email_on_failure' : True,
    'email_on_retry': True,
    'retries' : 1,
    'retry_delay' : timedelta(minutes = 5),
    }


dag = DAG(
    dag_id = 'ETL_toll_data',
    schedule_interval = dt.timedelta(days =1),
    default_args =  default_args,
    description = 'Apache Airflow Final Assignment',
    )



destination = "home/project/airflow/dags/finalassignment/staging"
source = os.path.join(DESTINATION,"tolldata.tgz")
vehicle_data = os.path.join(DESTINATION,"vehicle-data.csv")
tollplaza_data = os.path.join(DESTINATION,"tollplaza-data.tsv")
payment_data = os.path.join(DESTINATION,"payment-data.txt")
csv_data = os.path.join(DESTINATION,"csv_data.csv ")
tsv_data = os.path.join(DESTINATION,"tsv_data.csv")
fixed_width_data = os.path.join(DESTINATION,"fixed_width_data.csv")
extracted_data = os.path.join(DESTINATION, "extracted_data.csv")
transformed_data = os.path.join(DESTINATION, "staging/transformed_data.csv")




def download_dataset(url):
    wget.download(str(url),destination)
    return


def untar_tolldata(source,destination):
    try:
        with tarfile.open(source, "r:gz") as tgz:
            tgz.extractall(destination)
    except Exception as e:
        print(f"Error extracting {source}: {e}")





def extract_data_from_csv(input_file = vehicle_data, extracted_file = csv_data ):    
    
    global input_file
    print("Inside Extract")
    # Read the contents of the file into a string
    with open(input_file, 'r') as infile, \
            open(extracted_file, 'w') as outfile:
        for line in infile:
            fields = line.split(',')
            field_1 = fields[0]
            field_2 = fields[1]
            field_3 = fields[2]
            field_4 = fields[3]
            outfile.write(field_1 + "," + field_2 + "," + field_3 +  field_4 +"\n")

           
                



def extract_data_from_tsv(input_file = tollplaza_data, extracted_file = tsv_data ):    
    
     global input_file
    print("Inside Extract")
    # Read the contents of the file into a string
    with open(input_file, 'r') as infile, \
            open(extracted_file, 'w') as outfile:
        for line in infile:
            fields = line.split('/t')
            field_1 = fields[0]
            field_2 = fields[1]
            field_3 = fields[2]
            field_4 = fields[3]
            outfile.write(field_1 + "," + field_2 + "," + field_3 +  field_4 +"\n")



def extract_data_from_fixed_width(input_file = payment_data, extracted_file = fixed_width_data):    
    
     global input_file
    print("Inside Extract")
    # Read the contents of the file into a string
    with open(input_file, 'r') as infile, \
            open(extracted_file, 'w') as outfile:
        for line in infile.readlines():
            fields = line.split(" ")
            field_1 = fields[10]
            field_2 = fields[11]
            
            outfile.write(field_1 + "," + field_2 +"\n")




def consolidate_data(folder_path = [],consolidated_data = ):
    # replace with your folder's path
    
    all_files = os.listdir(folder_path)


    # Filter out non-CSV files
    csv_files = [f for f in all_files if f.endswith('.csv')]


    # Create a list to hold the dataframes
    df_list = []


    for csv in csv_files:
        file_path = os.path.join(folder_path, csv)
        try:
            # Try reading the file using default UTF-8 encoding
            df = pd.read_csv(file_path)
            df_list.append(df)
        except UnicodeDecodeError:
            try:
                # If UTF-8 fails, try reading the file using UTF-16 encoding with tab separator
                df = pd.read_csv(file_path, sep='\t', encoding='utf-16')
                df_list.append(df)
            except Exception as e:
                print(f"Could not read file {csv} because of error: {e}")
        except Exception as e:
            print(f"Could not read file {csv} because of error: {e}")


    # Concatenate all data into one DataFrame
    big_df = pd.concat(df_list, ignore_index=True)


    # Save the final result to a new CSV file
    big_df.to_csv(os.path.join(folder_path, 'combined_file.csv'), index=False)