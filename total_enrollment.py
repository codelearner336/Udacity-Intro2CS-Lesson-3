# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(list):
    total_enrollment = 0
    total_tuition = 0 
    for e in list:
        total_enrollment  = total_enrollment + e[1]
        total_tuition = total_tuition + e[1]*e[2]  # repeats for every element
    return total_enrollment,total_tuition





print total_enrollment(udacious_univs)
#>>> (90000,0)

print total_enrollment(usa_univs)
#>>> (77285,3058581079)
    
