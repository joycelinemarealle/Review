import math

def smallest_length_substring_with_sum(arr,s):
    window_start,min_length , window_sum =0, math.inf,0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s: #shrink again and again until sum <s. if take out elemt sum might still be greater than s. So multiple itieration
            #track the mini lenght of substring
            window_length = window_end - window_start +1
            min_length = min (window_length, min_length)
            #shrink remove first element and move window ahead
            window_sum -= arr[window_start]
            window_start +=1
    if min_length ==math.inf:
        return 0
    return min_length

if __name__ == '__main__':
    print(smallest_length_substring_with_sum([2,1,5,2,3,2],7))
    print(smallest_length_substring_with_sum([2,1,5,2,8],7))
    print(smallest_length_substring_with_sum([3,4,1,1,6], 8))

