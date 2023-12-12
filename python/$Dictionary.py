#A03 Dictionary

# Creating an empty dictionary
my_dict = {}

# Adding key-value pairs
my_dict['name'] = 'John'
my_dict['age'] = 30
my_dict['city'] = 'New York'
my_dict['name'] = 'Kevin'
# Displaying the dictionary
print("empty dict added values",my_dict)

my_dict = {'b': 3, 'a': 1, 'c': 2}
print("K01 : dict sort by keys asc - no value impact ",dict(sorted(my_dict.items())))
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_dict_by_keys_desc = dict(sorted(my_dict.items(), key=lambda item: item[0], reverse=True))
print("K02 : dict sort by keys desc - no value impact ",sorted_dict_by_keys_desc )



dChrVal = {'a': 1, 'b': 3, 'c': 2}

print("V01 dict sort by values asc", dict(sorted(dChrVal.items(), key=lambda item: item[1]))          )
print("V02 dict sort by values desc", dict(sorted(dChrVal.items(), key=lambda item: item[1], reverse=True)          ))

my_dict = {'b': 3, 'a': 1, 'c': 2}

# Sorting the dictionary by values in descending order
sorted_dict_by_values_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print ("rev sort dict fix", sorted_dict_by_values_desc)

#Highest element:
my_dict = {'b': 3, 'a': 1, 'c': 2}

# Find the key-value pair with the highest value
max_element = max(my_dict.items(), key=lambda item: item[1])
# Displaying the key-value pair with the highest value
print("Highest element:", max_element)


my_dict = {'b': 3, 'a': 1, 'c': 2}
# Initialize variables to store the maximum key-value pair
max_key = None
max_value = float('-inf')  # Start with negative infinity as the initial maximum value
# Iterate through each key-value pair in the dictionary
for key, value in my_dict.items():
    # Check if the current value is greater than the current maximum value
    if value > max_value:
        # If so, update the maximum key and value
        max_key = key
        max_value = value
# Display the key-value pair with the highest value
print("Highest element:", (max_key, max_value))






my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
keys_list = my_dict.keys()
print(keys_list )  # Output: dict_keys(['name', 'age', 'city'])

values_list = my_dict.values()
print(values_list)  # Output: dict_values(['John', 25, 'New York'])


#getting data from dictionary

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# Using square bracket notation
value = my_dict['key2']
print("value:")

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Using get() method
value = my_dict.get('key2')                   #value2
value = my_dict.get('keyx')   ; print(value)  #none
value = my_dict.get('keyx',0) ; print(value)  #0

#A04 2 D Array