#The expression not stack in Python is a way to check if a list (or any other container) is empty.
# When stack is an empty list, not stack evaluates to True. Otherwise, if stack contains any elements, not stack evaluates to False.

stack = []

print ("stack",stack )

y = not stack
print ("y ",y)
stack = ['A', 'B']
y = not stack
print ("y ",y)


