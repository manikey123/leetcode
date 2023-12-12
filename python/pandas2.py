# Writing data to a CSV file
data_to_insert = {'Name': ['John', 'Alice', 'Bob'],
                  'Age': [25, 30, 22],
                  'City': ['New York', 'London', 'Paris']}

import csv

csv_file_path = 'example.csv'

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(data_to_insert.keys())
    writer.writerows(zip(*data_to_insert.values()))

print(f'Data has been inserted into {csv_file_path}')
