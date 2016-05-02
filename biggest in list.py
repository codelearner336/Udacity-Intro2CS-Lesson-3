# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    
    if len(list_of_numbers)==0:
        return 0
    i=0
    greatest = (list_of_numbers[i]) #handles the case of a single element list and initial case
    while i< len(list_of_numbers)-1:
        greatest= bigger (greatest,list_of_numbers[i+1])
        i = i+1
    return greatest
            

def bigger (a,b):
    if a > b:
        biggerof2 = a
    else:
        biggerof2 = b
    return biggerof2
                  
print greatest([4,23,1,145,36])
print greatest([0])
print greatest ([2])
print greatest([3,2,1])
