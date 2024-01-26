#Python code to reverse an integer number

def revese_number (input):
      num=str(input)
      reverse_number=num[::-1]
      return num
     # reverse_number_int=int(reverse_number)


# use for loop ; use in reverse direction

# def reverse_number2(input):
#       ls =0
#       input = str(input)
#       for i in input[::-1]:
#            ls = ls*10 + int(i)
#       return ls

def reverse_number2(input):
      ls =0
      while input !=0:
            ls = ls*10 + input %10
            input= input //10
      return ls

num= 817
print (reverse_number2(num))

