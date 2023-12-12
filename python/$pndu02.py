import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Alice', 'Bob'],
        'Age': [25, 30, 22],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)