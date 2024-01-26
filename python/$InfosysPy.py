input_list = [3, 0, 0, 3, 12, 3]
move_element = 3

# Initialize lists for the specified element and others
specified_elements = []
other_elements = []

# Loop through the list and categorize each element
for num in input_list:
    if num == move_element:
        specified_elements.append(num)
    else:
        other_elements.append(num)

# Concatenate the lists
output = other_elements + specified_elements

print(output)



input_list = [3, 0, 0, 3, 12, 3]
move_element = 3

# Initialize a pointer for the position of the next non-move_element
insert_pos = 0

# Iterate through the list
for i in range(len(input_list)):
    if input_list[i] != move_element:
        # Swap the current element with the element at the insert position
        input_list[i], input_list[insert_pos] = input_list[insert_pos], input_list[i]
        # Move the insert position forward
        insert_pos += 1

print(input_list)