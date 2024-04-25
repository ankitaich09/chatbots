import pandas as pd

# Load the substances.csv file
df = pd.read_csv('substances.csv')

# Concatenate input and output rows with <eos> token
df['Text'] = df['Questions'] + ' <eos> ' + df['Answers']

# Save the concatenated data to a new CSV file
df[['Text']].to_csv('substances_one_col.csv', index=False)