# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(list1,element):
    i=0
    for e in list1:      # can be done with While     
        if e == element:
            return  i     # ends the program the first time you find element in list1
        i=i+1              
    return (-1)   # this happens if you complete the full loop without finding the answer        



print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'beta')
#>>> -1
