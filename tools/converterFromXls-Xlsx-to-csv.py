import os
import pandas as pd

# Set the directory where the Excel files are stored
directory = '../'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xls') or filename.endswith('.xlsx'):
        # Load the Excel file using pandas
        df = pd.read_excel(os.path.join(directory, filename))

        # Convert the DataFrame to CSV format
        csv_filename = os.path.splitext(filename)[0] + '.csv'
        df.to_csv(os.path.join(directory, csv_filename), index=False)
