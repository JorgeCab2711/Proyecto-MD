import os
import pandas as pd
import shutil

# Set the directories where the Excel files are stored and where the new files will be saved
directory = 'C:/Users/GAMING/Desktop/Proyecto MD'
new_directory = 'C:/Users/GAMING/Desktop/Proyecto MD/not converted'

# Create the new directory for unconverted files
os.makedirs(new_directory, exist_ok=True)

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.xls') or filename.endswith('.xlsx'):
        # Load the Excel file using pandas
        try:
            df = pd.read_excel(os.path.join(directory, filename))
        except:
            # If there is an error reading the file, move it to the new directory
            shutil.move(os.path.join(directory, filename),
                        os.path.join(new_directory, filename))
        else:
            # Convert the DataFrame to CSV format and save it in the original directory
            csv_filename = os.path.splitext(filename)[0] + '.csv'
            df.to_csv(os.path.join(directory, csv_filename), index=False)

            # Delete the original Excel file
            os.remove(os.path.join(directory, filename))
