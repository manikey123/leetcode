# Calculate the number of friends for each person
# given a relationship graph.
#
#
# For example:
#   The relationships amongst a set of friends
#   are shown in the graph below, where a line
#   between 2 nodes represents a friendship:
#
#                A ----- B ----- D
#                |       |
#                |       |
#                |       |
#                C ------/       E
#
#   This graph is represented as a list of
#   lists:
#      graph = [[A,B],[A,C],[C,B],[B,D],[E]]
#
#   The function "count_friends(graph)" should return
#   a dictionary object, where the Key is the
#   person's name and the Value is the number of
#   friends.
#
#   In the above example, the function should
#   return the following output:
#     {'A': 2, 'B': 3, 'C': 2, 'D': 1, 'E': 0}

def check_results(dict1, dict2):
   if len(dict1.keys()) != len(dict2.keys()):
       return 1
   for i in dict1.keys():
       if dict1[i] != dict2[i]:
           return 1
   return 0


assert check_results(count_friends([['A'],['B'],['C'],['D'],['E']]), {'A': 0, 'C': 0, 'B': 0, 'D': 0, 'E': 0}) == 0
assert check_results(count_friends([['A','B'],['C','D'],['E','F']]), {'A': 1, 'C': 1, 'B': 1, 'E': 1, 'D': 1, 'F': 1}) == 0
assert check_results(count_friends([['A','B'],['A','C'],['A','D'],['E']]), {'A': 3, 'C': 1, 'B': 1, 'E': 0, 'D': 1}) == 0
assert check_results(count_friends([['A','B'],['A','C'],['C','B']]), {'A': 2, 'C': 2, 'B': 2}) == 0
assert check_results(count_friends([['A','B'],['A','C'],['C','B'],['B','D'],['E']]), {'A': 2, 'C': 2, 'B': 3, 'E': 0, 'D': 1}) == 0
print('passed')
