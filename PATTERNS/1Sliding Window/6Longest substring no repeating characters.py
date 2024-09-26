def longest_substring_no_repeating_characters(str):
    #1 Initialization
    window_start = 0
    max_length = 0
    char_freq ={} #empty dictionary to hold frequency

    #2 Sliding window
    for window_end in range(len(str)):

        #3 Checking each character in the string
        right_char = str[window_end]

        if right_char not in char_freq:
            char_freq[right_char] = 1
        else:
            char_freq[right_char] +=1

        #4 Shrink window when character repeats
        while char_freq[right_char] > 1:
            left_char = str[window_start]
            char_freq[left_char] -=1 #shrinking window, remove freq in dict
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start +=1 #move window ahead
        #5 Track max length
        max_length = max(max_length, (window_end- window_start +1))
    return max_length

if __name__ == '__main__':
    str = "aabccbb"
    print(longest_substring_no_repeating_characters(str))


