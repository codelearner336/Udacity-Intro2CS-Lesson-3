
test = [1,2,3,4,5,6,7,7]

def dup_list(list):
    n= len(list)
    i=0
    while i < n:
        j=i+1 
        while j < n: 
             print i,j              #verify the full loop is run 
             if test[i] == test[j]:
                  return False
             else:
                  j =j+1
        i=i+1
    return True
    
print dup_list(test)
