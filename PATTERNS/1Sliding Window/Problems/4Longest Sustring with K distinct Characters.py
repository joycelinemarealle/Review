#str = string array with letters
#k number of distinct no
def longest_substring_with_k_distinct(str,k):
    #intialization
    window_start = 0
    max_length = 0
    char_frequency = {} # dictionary keep track of each character in current window

    # 2 Sliding window through the str array
    # in the loop we will try to extend the range between [window_start, window_end]
    for window_end in range (len(str)):

        #3 Process each character
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 1 #first time
        else:#if character exists already
            char_frequency[right_char] +=1
    #4 Shrink the sliding window, until we are left with k distinct characters in the char_frequency
        while len(char_frequency) > k: #if distinct character in dict > k
            left_str= str[window_start]
            char_frequency[left_str] -=1 #shrink the windowreduce frequency since removing element going out
            if char_frequency[left_str] == 0:
               del char_frequency[left_str] #freq iz zero then character no longer in window
            window_start +=1 #move window ahead
           #remember  the maximum length so far
        max_length = max(max_length, window_end-window_start +1)
    return max_length
if __name__ == '__main__':
    str ="araaci"
    k = 2
    print (longest_substring_with_k_distinct(str,k))