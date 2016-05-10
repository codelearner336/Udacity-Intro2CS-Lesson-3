
incorrect = [[1,2,3,4],[2,3,1,4],[4,1,2,3],[4,2,3,1]]

correct = [[1,2,3], [2,3,1], [3,1,2]]

incorrect1 = [[0,2,3,4],[2,3,1,4],[4,1,2,3],[4,2,3,1]]
incorrect2 = [[5,2,3,4],[2,3,1,4],[4,1,2,3],[4,2,3,1]]


def check_sudoku(test):


# range check  - numbers should not be greater than the length of the list 

    n = len(test)
    h = 0
    i = 0
    while h < n:
        while i < n:
                
                if test[h][i] > n:
                    #print test [h][i]
                    print "error - the value of the number is too darn high "
                    return False
                else:
                     #print test[h][i]
                     i=i+1
        h = h+1
        i=0
        
# range check  - numbers should not be less than zero list

    print "range check 1 ok"
    h=0
    i=0
    while h < n:
        while i < n:
                
                if test[h][i] < 1:
                    #print test [h][i]
                    print "error - value found less than 1"
                    return False
                else:
                     #print test[h][i]
                     i=i+1
        h = h+1
        i=0
    print "range check 2 ok"
# this checks for duplicates in the subssets i.e. the rows
     
    n = len(test)
    h = 0
    while h < n:
         i=0
         while i < n:
             j=i+1 
             while j < n: #otherwise miss the last element
                  #print h,i,h,j  #verify full loop is executed
                  if test[h][i] == test[h][j]:
                       print "rows check - error found" 
                       return False
                  else:
                         j =j+1
             i=i+1
         h=h+1   
    print "check rows ok"
# this checks for duplicates in the columns
     
    h = 0
    i = 0
    while h < n:
        while i < n:
              k = h+1
              while k < n:
                     #print h,i,k,i
                     if test[h][i] == test [k][i]:
                          print "columns check - error found"
                          return False
                     else:
                          k = k+1
              i = i+1
        h = h+1
        i=0
    print "check columns ok"    
    return True
             
# could add an integer check and could solve this by just checking for integers 1 to n in each row and column    
print check_sudoku(incorrect)
print check_sudoku(incorrect1)
print check_sudoku(incorrect2)
print check_sudoku(correct)
