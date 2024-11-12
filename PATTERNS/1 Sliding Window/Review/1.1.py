
def aveg_sublist_size_k(arr, k):
    window_sum = 0
    window_start =0
    aveg_array = []

    #slide window over array
    for window_end in range(len(arr)):
       window_sum += arr[window_end] #add next element
       #shrink window when size > k
       # shrink window when condition met
       if window_end - window_start +1 >= k:
            #find aveg
            aveg = window_sum/k
            aveg_array.append(aveg)
            #remove first element and move the window_start ahead +=1
            window_sum -= arr[window_start]
            window_start +=1
    return aveg_array

if __name__ =='__main__':
    print(aveg_sublist_size_k([1,3,2,6,-1,4,1,8,2],5))