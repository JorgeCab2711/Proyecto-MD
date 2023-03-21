import os
import pandas as pd

# Set the directory where the CSV files are stored
directory = 'C:/Users/GAMING/Desktop/Proyecto MD'

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Load the CSV file using pandas, skipping the first row
        df = pd.read_csv(os.path.join(directory, filename),
                         skiprows=[0], encoding='utf-8')

        # Remove the "Código CIE-10" column if it exists
        if "Código CIE-10" in df.columns:
            df = df.drop("Código CIE-10", axis=1)

            # Save the modified DataFrame to the original CSV file
            df.to_csv(os.path.join(directory, filename),
                      index=False, encoding='utf-8')
