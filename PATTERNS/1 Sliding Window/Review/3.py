import math

def smallest_length_substring_with_sum(arr,s):
    # Initialization
    window_start, window_sum, min_length = 0,0,math.inf

    #Sliding window
    for window_end in range (len(arr)):
        window_sum += arr[window_end] #add next element

        #shrink window as small as possible until window_sum is smaller than s
        while window_sum >= s: #as long as condition met keep doing below
            #track length see if minimum
            min_length = min (min_length,window_end-window_start+1)
            #minus element from sum
            window_sum -= arr[window_start]
            window_start+=1 #slide ahead
    if min_length == math.inf:
        return 0
    return min_length

if __name__ == '__main__':
    print(smallest_length_substring_with_sum([2,1,5,2,3,2],7))
    print(smallest_length_substring_with_sum([2,1,5,2,8],7))
    print(smallest_length_substring_with_sum([3,4,1,1,6], 8))
