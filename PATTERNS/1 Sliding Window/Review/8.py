def longest_subarray_with_ones_after_replacement(arr,k):
    # 1.py Initialization
    window_start = 0
    max_length = 0
    ones_count = 0

    # 2 Slide window
    for window_end in range(len(arr)):
        if arr[window_end] ==1:
            ones_count +=1

        while window_end-window_start +1 - ones_count > k:
            #rebalance counts
            if arr[window_start] ==1 :
                ones_count -=1

                #move ahead
            window_start +=1
    max_length = max (max_length, window_end-window_start+1)

    return max_length

if __name__ == '__main__':
    print(longest_subarray_with_ones_after_replacement([0,1,1,0,0,0,1,1,0,1,1],2))

