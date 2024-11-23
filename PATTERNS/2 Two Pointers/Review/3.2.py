# [-2,-1,0,2,3]
def sorted_squares_array(arr):
    left = 0
    n = len(arr)
    right = n -1
    square_array = [0 for x in range (len(arr))] #empty array of fixed size
    squares_highest_index = n-1

    while left < right:
        left_squares = arr[left] * arr[left]
        right_squares = arr[right] * arr[right]

        if left_squares > right_squares:
            square_array[squares_highest_index] = left_squares
            left+=1
        else:
            square_array[squares_highest_index] = right_squares
            right -=1
        squares_highest_index -=1
    return square_array
#deal with sorting squares of -ves> +ves so if positive
#left point = 0 , right pointer lne(arr)-1
#empty array to store squares
#if squares -ve < +ve then appen move left+=1
#if squares of -ve greater +ve then append using +ve squares move right -=1

