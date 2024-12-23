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

#>>>> New Code block

def extract_data_from_csv(input_file=vehicle_data, extracted_file=csv_data):
    print("Inside Extract")

    # Open the input CSV file for reading and the output CSV file for writing
    with open(input_file, 'r') as infile, open(extracted_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for fields in reader:
            # Ensure there are at least four fields before accessing them
            if len(fields) >= 4:
                field_1 = fields[0]
                field_2 = fields[1]
                field_3 = fields[2]
                field_4 = fields[3]

                # Write the selected fields to the output CSV file
                writer.writerow([field_1, field_2, field_3, field_4])

    print(f"Data extracted to {extracted_file}")

           
                



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


#>>>>>New code block for tsv

def extract_data_from_tsv(input_file='tollplaza_data.tsv', extracted_file='extracted_data.csv'):
    print("Inside Extract")

    # Open the input TSV file for reading and the output CSV file for writing
    with open(input_file, 'r') as infile, open(extracted_file, 'w', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile)

        for fields in reader:
            # Ensure there are at least four fields before accessing them
            if len(fields) >= 4:
                field_1 = fields[0]
                field_2 = fields[1]
                field_3 = fields[2]
                field_4 = fields[3]

                # Write the selected fields to the output CSV file
                writer.writerow([field_1, field_2, field_3, field_4])

    print(f"Data extracted to {extracted_file}")








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



#>>>>> new code block for fixed width

def extract_data_from_fixed_width(input_file=payment_data, extracted_file=extracted_data):
    print("Inside Extract")
    
    # Define the start and end positions of the fields in the fixed-width format
    field_1_start, field_1_end = 10, 20  # Example positions for field_1
    field_2_start, field_2_end = 21, 31  # Example positions for field_2
    
    # Open the input file for reading and the output CSV file for writing
    with open(input_file, 'r') as infile, open(extracted_file, 'w') as outfile:
        for line in infile:
            # Extract fields using slicing based on fixed positions
            field_1 = line[field_1_start:field_1_end].strip()
            field_2 = line[field_2_start:field_2_end].strip()

            # Write the extracted fields to the output CSV file
            outfile.write(field_1 + "," + field_2 + "\n")
    
    print(f"Data extracted to {extracted_file}")





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





    #>>>>> Consolidate data

    import csv

def consolidate_data(csv_file=csv_data, tsv_file=tsv_data, fixed_width_file=fixed_width_data, output_file=extracted_data):
    # Define the headers in the order specified
    headers = [
        'Rowid', 'Timestamp', 'Anonymized Vehicle number', 'Vehicle type', 
        'Number of axles', 'Tollplaza id', 'Tollplaza code', 
        'Type of Payment code', 'Vehicle Code'
    ]

    # Initialize an empty list to collect all rows of data
    consolidated_data = []

    # Helper function to read CSV data and add it to the consolidated data list
    def read_and_add_data(file_name):
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Reorder the fields according to the headers list
                ordered_row = [row.get(header, '') for header in headers]
                consolidated_data.append(ordered_row)

    # Read data from each input file
    read_and_add_data(csv_file)
    read_and_add_data(tsv_file)
    read_and_add_data(fixed_width_file)

    # Write the consolidated data to the output CSV file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(headers)
        # Write all data rows
        writer.writerows(consolidated_data)

    print(f"Data consolidated into {output_file}")

# Example usage
consolidate_data()






def transform_data(input_file=extracted_data, output_file=transformed_data):
    # Open the input CSV file for reading
    with open(input_file, 'r') as infile:
        reader = csv.DictReader(infile)
        
        # Open the output CSV file for writing
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            
            # Write the header row
            writer.writeheader()
            
            # Process each row in the input file
            for row in reader:
                # Transform the vehicle_type field to uppercase
                if 'Vehicle type' in row:
                    row['Vehicle type'] = row['Vehicle type'].upper()
                
                # Write the transformed row to the output file
                writer.writerow(row)

    print(f"Data transformed and saved to {output_file}")

# Example usage
transform_data()
