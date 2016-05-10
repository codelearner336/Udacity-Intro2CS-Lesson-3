
incorrect = [[1,2,3,4],[2,3,1,4],[4,1,2,3],[4,2,3,4]]

correct = [[4,5,6], [5,6,4], [6,4,5]]
test = [1,2,3,4,5,6,7,8]

def check_sudoku(test):

# this checks for duplicates in the subssets i.e. the rows
     
    n= len(test)
    h=0
    while h < n:
         i=0
         while i < n:
             j=i+1 
             while j < n: #otherwise miss the last element
                  print h,i,h,j  #verify full loop 
                  if test[h][i] == test[h][j]:
                       return False
                  else:
                         j =j+1
             i=i+1
         h=h+1   
    print "checkpoint 1"
# this checks for duplicates in the columns
     
    h=0
    i=0
    while h < n:
        while i<n:
              k=h+1
              while k < n:
                     print h,i,k,i
                     if test[h][i] == test [k][i]:
                          return False
                     else:
                          k = k+1
              i=i+1
        h=h+1
        i=0
    return True
             
    
print check_sudoku(incorrect)
   
print check_sudoku(correct)
