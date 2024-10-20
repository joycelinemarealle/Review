def squares_of_array(arr):

    #initialization
    n= len(arr)
    left , right = 0, n-1 #pointers
    squares = [0 for x in range(n)]#empty sized defined array
    squares_highest_index =n-1 #index of last element in squares arry

    # 2 loop through array
    while left <= right:
        # 3 Compare squares
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]
        if leftSquare > rightSquare:
            squares[squares_highest_index] = leftSquare
            left +=1     #move the pointer
        else:
            squares[squares_highest_index] = rightSquare
            right -= 1  #move right pointer
        squares_highest_index -=1
    return squares
if __name__ == '__main__':
    print(squares_of_array([-2,-1,0,2,3]))



