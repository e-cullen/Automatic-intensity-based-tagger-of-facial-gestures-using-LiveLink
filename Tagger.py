import numpy as np
import pandas as pd

#Input your file name here
FILE = ' .csv'

df = pd.read_csv(FILE)

# Input your desired blendshape to be tagged, ensure the capitalization matches the column name in the CSV
chosen_unidirectional_blendshape = ''
# Input your desired intensity threshold value, e.g., 0.3
chosen_threshold = 


# Define the tagging function
def tag(row):
    # Access the value of the chosen blendshape for the current row
    if row[chosen_unidirectional_blendshape] >= chosen_threshold:
        return f'Tagged - {chosen_unidirectional_blendshape}'
    else:
        return ''


# Apply the function to each row in the DataFrame
df['BlendshapeTagged'] = df.apply(tag, axis=1)

# Save the updated DataFrame to a CSV file
output_file = f'{chosen_unidirectional_blendshape}_Tagged.csv'
df.to_csv(output_file, index=False)
print(f"Tagged data saved to {output_file}")
