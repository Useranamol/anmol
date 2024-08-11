import pandas as pd

df = pd.read_json('students.json')

# Convert the dictionary to a DataFrame
df = pd.DataFrame(list(df["students"].items()), columns=["ID", "Name"])

# Save the DataFrame to an Excel file
file_path = "students.xlsx"
df.to_excel(file_path, index=False)