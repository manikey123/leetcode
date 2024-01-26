# given two lists output the words that don't exist in both lists


list1 = ['chakra', 'mudra', 'sleep']
list2 = ['chakra', 'mudra', 'thirdeye']


print(list(set(list1).difference(list2)))

print(list(set(list1).intersection(list2)))



