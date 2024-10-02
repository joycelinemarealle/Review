def aveg_subarray(arr,k):
    #1initialization
    window_start = 0
    aveg_array = []
    total_sum = 0

    #2Slide window outer loop goes t last element which will have k size
    for window_end in range(len(arr)):
        total_sum += arr[window_end] #add next element
    #3 When window when size of window >= k calculate aveg sum + shrink + slide ahead
        if window_end-window_start +1 >= k:
            aveg = total_sum / k
            aveg_array.append(aveg)  # add to array
            total_sum -= arr[window_start] #minus element going out
            window_start +=1 #slide window ahead
    return aveg_array

if __name__ == '__main__' :
       print(aveg_subarray([1,3,2,6,-1,4,1,8,2], 5))