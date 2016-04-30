# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(list_of_strings):
  
    count_of_startingletter_u = 0
    for e in  list_of_strings:
       #print e[0]
       if e[0] == "U":
          count_of_startingletter_u = count_of_startingletter_u + 1
    return count_of_startingletter_u        
    
print measure_udacity(['Dave','Sebastian','UKaty'])
#>>> 1

print measure_udacity(['Umika','Umberto'])
#>>> 2
