def length_longest_substring(arr,k):
    #1 Initialization of variables
    window_start, max_length , max_ones_count = 0,0,0

    #2 sliding the window
    for window_end in range (len(arr)):

        #3 go through each number and update dictionary + max_ones_count
        if arr[window_end] == 1:
            max_ones_count +=1

        #4 shrink window when number remaining needed to replace > k
        #track the count of ones keep track max,
        if ( window_end- window_start+1 - max_ones_count) > k:
           if arr[window_start] ==1:
               max_ones_count-=1 #reduce the frequency of ones
           window_start +=1

        #5Track max_length
        max_length = max(max_length, window_end - window_start +1)
    return max_length

if __name__ == '__main__':
    print(length_longest_substring([0,1,1,0,0,0,1,1,0,1,1],2))

