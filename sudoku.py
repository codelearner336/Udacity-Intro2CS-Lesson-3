
incorrect = [[1,2,3,4],[2,3,1,4],[4,1,2,3],[4,2,3,4]]

correct = [[4,5,6], [5,6,4], [6,4,5]]
test = [1,2,3,4,5,6,7,8]

def check_sudoku(test):

# this checks for duplicates in the subssets i.e. the rows, but not the columns
     
    n= len(test)
    h=0
    while h < n:
         i=0
         while i < n:
             j=i+1 
             while j < n: #otherwise miss the last element
                  print h,i,j  #verify full loop 
                  if test[h][i] == test[h][j]:
                       return False
                  else:
                         j =j+1
             i=i+1
         h=h+1   
    return True


             
    
print check_sudoku(incorrect)
   
print check_sudoku(correct)
