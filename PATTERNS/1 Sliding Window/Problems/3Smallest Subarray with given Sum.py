#s = sum
# arr input of numbers
import math
def smallest_subarray_with_given_sum(s,arr):
    #size of window changes
    #find sum of elements until sum >= s
    window_sum = 0
    window_start = 0
    min_length = math.inf #start with infinity

    for window_end in range (len(arr)):
        #sum next element
        window_sum += arr[window_end]

        #shrink the window as small as possible until < sum
        while window_sum >= s:
            #check if current length min
            min_length = min(min_length, (window_end - window_start +1))#number of elements in sublist

            #substrack first element to shrink the sliding window
            window_sum -= arr[window_start]

            #slide ahead
            window_start +=1

    if min_length == math.inf:
        return 0
    return min_length
if __name__ == '__main__':
    arr = [2,1,5,1,3,2]
    s= 3
    print(smallest_subarray_with_given_sum(s,arr))

