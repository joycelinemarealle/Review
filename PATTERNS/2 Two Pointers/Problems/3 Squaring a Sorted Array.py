def make_squares(arr):
    #1 initialization
    n = len(arr) # size of array
    squares = [0 for x in range(n)] #array of zeros + same size to store result
    squares_Highest_Index = n-1 #fill squARES ARRAY FROM END =
    left, right = 0, n-1 #two pointers

    #2 Process array
    while left <= right: # = when one element left to process
        leftSquare = arr[left] * arr[left]
        rightSquare = arr[right] * arr[right]

    #3 Compare squares and fill squares array
        if leftSquare > rightSquare:
            squares[squares_Highest_Index] = leftSquare # Put the larger square into the squares array
            left+=1 # Move the left pointer to the next element

        else:
            squares[squares_Highest_Index] = rightSquare
            right -=1 # Move right pointer to the next element
    #4 Decrease highest index
        squares_Highest_Index -=1
    #5 Return array
    return squares

if __name__ == '__main__':
    print(make_squares([-2,-1,0,2,3]))

