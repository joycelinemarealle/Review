def max_sum_of_subarray(arr,k):
    #1 Initialization
    window_start, max_sum , window_sum = 0,0,0
    
    #2 Slide window
    for window_end in range ( len(arr)):
        window_sum += arr[window_end]

        #3 Shrink window
        if window_end-window_start +1 >= k:
            #4 track max window_sum
            max_sum = max(max_sum, window_sum)

            #minus element going out
            window_sum -= arr[window_start]

            #move window ahead
            window_start +=1
    return max_sum

if __name__ == '__main__':
    print(max_sum_of_subarray([2,1,5,1,3,2],3))
    print(max_sum_of_subarray([2,3,4,1,5],2))
