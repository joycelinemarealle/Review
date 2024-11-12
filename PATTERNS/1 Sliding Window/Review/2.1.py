def max_sum_of_subarray_size_k(arr,k):
    window_start, max_sum, window_sum = 0,0,0
    for window_end in range (len(arr)):
        window_sum += arr[window_end]
        if window_end-window_start +1 >=k:
            #find max sum
             max_sum = max(max_sum, window_sum)

            #shrink window and remove 1st element
             window_sum-= arr[window_start]
             window_start +=1
    return max_sum
if __name__ == '__main__'  :
    print(max_sum_of_subarray_size_k([2,1,5,1,3,2],3))