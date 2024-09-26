def max_sub_array_of_size_k(k,arr):
    max_sum = 0
    window_sum = 0
    window_start = 0

    #slide the window through the array
    for window_end in range (len(arr)):
        window_sum += arr[window_end]

        #Slide when size of window is reached
        if window_end >= k-1:
            #find max sum
            max_sum = max(max_sum, window_sum)
            #remove element going out
            window_sum -= arr[window_start]
            #slide window ahead
            window_start +=1
    return max_sum
if __name__ == '__main__':
    arr = [2,1,5,1,3,2]
    k= 3
    print(max_sub_array_of_size_k(k,arr))