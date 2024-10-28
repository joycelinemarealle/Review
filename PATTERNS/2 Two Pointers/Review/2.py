def remove_duplicates(arr):
    #initialization
    next_non_duplicate, i = 1,1

    #Iterate through the array
    while i < (len(arr)):
        #compare first element to element iterator has
       if  arr[next_non_duplicate-1] != arr[i]:
           arr[next_non_duplicate] = arr[i]
           next_non_duplicate +=1
       #move iterator
       i +=1
    return next_non_duplicate
if __name__ == '__main__':
    print(remove_duplicates([2,3,3,3,6,9,9]))
    print(remove_duplicates([2, 2,2,11]))


