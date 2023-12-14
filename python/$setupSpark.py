import pandas as pd

# Create a DataFrame
# data = {'Name': ['John', 'Alice', 'Bob'],
#         'Age': [25, 30, 22],
#         'City': ['New York', 'London', 'Paris']}
#
# df = pd.DataFrame(data)

# # Display the DataFrame
# print("DataFrame:")
# print(df)

datalist = [
    [1, 'Mak', 35],
    [2, 'Dee', 33],
    [3, 'Moh', 69],
    [4, 'Mal', 66],
    [5,'Man', 32]
]

# Creating a DataFrame from the list
df2 = pd.DataFrame(datalist, columns=['ID', 'Name', 'Age'])
print(df2)

df2['Gender'] = ['Male', 'Female', 'Male', 'Female', 'Female']
print(f"Original dataframe odf2 \n {df2}")



print("df direct filter gives true false ", df2['Age'] > 40 , "cow")
df_filtered = df2[df2['Age'] > 40] ; print("filter age is 40",df_filtered)
print("df2", df2) #not affected by filtering
dfMale = df2[df2['Gender']=='Male'] ; print("dfMale", dfMale)

#records

#iloc
print ("1",df2.iloc[0])          # Selects the first row
print ("2",df2.iloc[:, 0])       # Selects the first column
print ("3",df2.iloc[1:3, :])      # Selects rows 1 to 2 and all columns
print ("4",df2.iloc[:, [0, 2]])  # Selects all rows and columns 0 and 2

#loc
print ("5",df2.loc[0])           # Selects the row with label 0
print ("6",df2.loc[:, 'Name'] )  # Selects the column with label 'Name'
print ("7",df2.loc[1:3, :] )      # Selects rows with labels 1 to 3 and all columns
print ("8",df2.loc[:, ['Name', 'Age']])  # Selects all rows and columns 'Name' and 'Age'

print("read second row of dataframe loc \n", df2.loc[1])
print("read second row of dataframe \n", df2.iloc[1])
print("read second row and second element of dataframe", df2.iloc[1][1])
print("read two rows of dataframe head2 \n", df2.head(2), "tail \n", df2.tail(2) )
print("df info \n", df2.info)

#Sorting
sorted_df = df2.sort_values(by='Age') ; print('sort by age ascending \n', sorted_df)# ;
sorted_df_desc = df2.sort_values(by='Age', ascending=False) ; print('sort by age desc \n',sorted_df_desc)
sorted_df_descHead2 = df2.sort_values(by='Age', ascending=False).head(2) ; print('sort by age Head2 \n',sorted_df_descHead2)

# Calculate mean and median age
mean_age = df2['Age'].mean()
median_age = df2['Age'].median()
print(f"Mean Age: {mean_age}, Median Age: {median_age}")

#
# #Groupings
min_age = df2['Age'].min() ; max_age = df2['Age'].max() ; average_age = df2['Age'].mean()
print(f'Minimum Age: {min_age} MaxAge :{max_age} , AverageAge: {average_age}')

print (df2)
gender_counts = df2['Gender'].value_counts() ; print('gender male-female count \n',gender_counts)
group_by_gender = df2.groupby('Gender') ;      print("gender group1 ", group_by_gender)
group_by_gender2 = df2.groupby('Gender')['Age'].mean() ; print("gender group2", group_by_gender2)

result = df2.groupby('Gender').filter(lambda x: x['Age'].mean() > 40) ; print('Average age above 40 \n',result)
