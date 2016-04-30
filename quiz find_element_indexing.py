# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list1,element):
   # print list1.index(element)
   # print element in list1      #e in p
   # print element not in list1  # e not in p 
   # print not element in list1  # not e in p
    
    if element in list1:                # or do if not and then return -1 
        return list1.index(element) 
    else:
        return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'beta')
#>>> -1
