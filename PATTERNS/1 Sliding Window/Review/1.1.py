
def aveg_sublist_size_k(arr, k):
    total_sum = 0
    for window_start in range (len(arr) -k):
        for window_end in range(window_start,len(arr)-1):
            total_sum += arr[window_end]
            #shrink window when size > k
            while window_end - window_start +1 == 5:
                #find aveg
                aveg = total_sum/k
                # move the window_start ahead +=1
                window_start +=1

    return aveg

if __name__ =='__main__':
    print(aveg_sublist_size_k([1,3,2,6,-1,4,1,8,2],5))