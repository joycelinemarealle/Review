def sorted_squares_array(nums):
    #Initialization
    #left , right pointer , empty array of length pf element

    n = len(nums)
    left,right = 0, n-1
    squares = [0 for x in range (n) ] #[0,0,0,0,0]
    max_index_of_squares = n-1

    # loop through the array and compare left nad right squares
    while left <= right:
        left_squares = nums[left] * nums[left]
        right_squares = nums[right] * nums[right]
        #if left > right square then save as the last element in square array
        if left_squares > right_squares:
            squares[max_index_of_squares] = left_squares
            # move left pointer forward
            left +=1
        else:
            #save the element in the position largest index of square array
            squares[max_index_of_squares] = right_squares
            right -=1
            #move right pointer backward
        #index -=1
        max_index_of_squares -=1
    return squares
if __name__ == '__main__':
   print( sorted_squares_array([-2,-1,0,1,2]))