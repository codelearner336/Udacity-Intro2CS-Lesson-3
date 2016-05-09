
test = [1,2,3,4,5,6,7,8]

def dup_list(list):
    
    if len (set(test)) != len (test):
        return (False)
    else:
        return (True)


print dup_list(test)
