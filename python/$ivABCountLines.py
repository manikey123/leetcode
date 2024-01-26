'''
Write a program that does the following:
Accept the following inputs:
(1) Number of nodes
(2) A 2-D array representing edges. ith edge connects node input2[0][i] to node input2[1][i].
Assuming that a line can be drawn between nodes if there is an edge between them, print number of lines that can be drawn between nodes.

Sample test case:
input1: 4
input2: {{1,1,1},{2,3,4}}
output1: 3

This file should contain many test cases. Each test case should be different in some way. To help you work out the problem holistically, think about at least 4 different positive test cases and at least 2 test cases that result in some error message.

Please note that both inputs are to be used.

Template for a test case is as follows:
input1: A
input2: B
output: C
Reason: Output is C because <give reason here>.

Example is given below:

Test case 1:
input1: 4
input2: {{1,1,1},{2,3,4}}
output: 3
Reason: The output is 3 since the following 3 lines can be drawn (1,2), (1,3), (1,4).

'''
def count_lines(nodes, edges):
    # Create a set to store unique edges
    unique_edges = set()

    # Check if the edges array is not empty and has valid structure
    if not edges or len(edges) != 2 or any(len(edge) != len(edges[0]) for edge in edges):
        return "Invalid edge list"

    # Iterate through the edge list
    for i in range(len(edges[0])):
        # Check if nodes are within the valid range
        if not (1 <= edges[0][i] <= nodes and 1 <= edges[1][i] <= nodes):
            return "Invalid node in edges"

        # Add the edge as a tuple to the set (sort the tuple to avoid duplicate edges)
        unique_edges.add(tuple(sorted((edges[0][i], edges[1][i]))))

    # The number of unique edges is the number of lines that can be drawn
    return len(unique_edges)


# Test cases
test_cases = [
    (4, [[1, 1, 1], [2, 3, 4]], 3, "The output is 3 since the following 3 lines can be drawn (1,2), (1,3), (1,4)."),
    (3, [[1, 2], [2, 3]], 2, "The output is 2 since the following 2 lines can be drawn (1,2), (2,3)."),
    (4, [], 0, "The output is 0 since no edges are given."),
    (5, [[1, 2, 3, 4], [2, 3, 4, 5]], 4,
     "The output is 4 since there are 4 unique lines connecting each consecutive node."),
    (6, [[1, 2, 3, 4, 5, 1], [2, 3, 4, 5, 6, 6]], 6, "The output is 6 since each node is connected forming a loop."),
    # Error cases
    (4, [[1, 2, 3], [2, 3]], "Invalid edge list", "Error due to unequal length of edge pairs."),
    (3, [[0, 2], [2, 3]], "Invalid node in edges", "Error due to node number 0, which is out of valid range."),
]

# Run test cases
for i, (nodes, edges, expected_output, reason) in enumerate(test_cases, 1):
    result = count_lines(nodes, edges)
    print(f"Test case {i}: ")
    print(f"input1: {nodes}")
    print(f"input2: {edges}")
    print(f"output: {result}")
    print(
        f"Reason: {reason if result == expected_output else 'Unexpected result, should have been ' + str(expected_output)}.")
    print()
