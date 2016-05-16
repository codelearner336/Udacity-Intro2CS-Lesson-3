

# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal 
# to the preceding number y, the number x should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist if they are less than the last number .
# When you reach a number greater than the previous numberm add
# that number to the main list. repeat till all numbers handled


#Hint - "int()" turns a string's element into a number

def numbers_in_lists(message):

    result = [int(message[0])] 
    sublist = []

    x=0
    y=x+1
    sublistflag = 0  # flag is 1 when you are in the sublist
    while y < len(message):
     if sublistflag ==0:   
            if int(message[y]) > int(message[x]):
                result.append(int(message[y]))
                x=x+1
                y=x+1
            else:   
                    sublistflag = 1
                    sublist.append(int(message[y]))
                    x=x+1
                    y=x+1
     else:   # loop for flag=1
         if int(message[y]) > int(sublist[0]):
                result.append(sublist)
                sublistflag = 0
                sublist = []
                result.append(int(message[y])) # when existing the sublist I append it to the main list. This is the only time the sublist should be appended
                x=x+1
                y=x+1
         else:   
             sublist.append(int(message[y]))
             
             x=x+1
             y=x+1

    if sublistflag == 1:        # this is needed to handle the case when the last element in the list is being put in a sublist. If the while loop completes then this executes 
       result.append(sublist)
              
    return result

print numbers_in_lists("455532123266")

print numbers_in_lists("543987")
