from __future__ import division

def list_mean(numbers):

    if numbers == []:
        return "empty list has no mean" 
    else:
        list_mean = sum(numbers) / len(numbers)
        return list_mean


print list_mean([1,2,3,4])
print list_mean([1,3,4,5,2])
print list_mean([2])
print list_mean([])

