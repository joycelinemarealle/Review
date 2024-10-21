def find_averages_of_subarrays(K,arr):
    result =[]
    window_sum = 0
    window_start = 0

    #Slide window over the array
    for window_end in range (len(arr)):
        window_sum += arr[window_end] #add next element

        #Slide the window, when we hit the required window size
        if window_end >= K-1:#index 4 = elements 5
            result.append(window_sum/K)
            #remove first element
            window_sum -= arr[window_start] #subtract element going out
            window_start +=1 #slide window ahead
    return result


if __name__ == '__main__':
    arr = [1,3,2,6,-1,4,1,8,2]
    K= 5
    print(find_averages_of_subarrays(K,arr))
