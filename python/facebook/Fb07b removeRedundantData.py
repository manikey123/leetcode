# Remove redundant data from a list

def remove_redudant_data(b):
      c=[]
      for i  in b:
            if i not in c:
               c.append(i)
      return c

