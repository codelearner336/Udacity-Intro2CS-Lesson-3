# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    
    greatest = 0
    for e in list_of_numbers:
        if e > greatest:
            greatest = e
    return greatest        
                  
print greatest([4,23,1,145,36])
print greatest([0])
print greatest ([2])
print greatest([3,2,1])
