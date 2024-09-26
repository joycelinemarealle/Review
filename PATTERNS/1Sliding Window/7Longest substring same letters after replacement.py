from locale import windows_locale


def length_longest_substring(str):
    #1 intialization
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    char_freq = {}

    #2 sliding the window
    for window_end in range (len(str)):
        #3 Go through each character in the str array
        right_char = str[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 1
        else:
            char_freq[right_char] +=1

        #trackmax frequency
        max_repeat_letter_count = max(max_repeat_letter_count, char_freq[right_char])
       if ( window_end -window_start +1 - max_repeat_letter_count) > k:
           left_char = str[window_start]
           char_freq[left_char] -= 1
           window_start +=1
       max_length =  max(max_length, windows_end-window_end +1)
    return max_length