def longest_substring_after_replacement(str,k):

    #1Initialization
    window_start =0
    max_repeated_letter_count = 0
    max_length = 0
    char_freq = {}

    #2 Slide window
    for window_end in range (len(str)):

        #3 Process each char to put in hashmap
        right_char = str[window_end]
        if right_char not in char_freq:
            char_freq[right_char] =1
        else:
            char_freq[right_char] +=1

        max_repeated_letter_count = max(max_repeated_letter_count, char_freq[right_char])

        #4 Shrink window when remaining char to be replaced > k
        while (window_end -window_start +1 - max_repeated_letter_count) > k: #shrink once
            #rebalance hashmap
            left_char = str[window_start]
            char_freq[left_char] -=1
            if char_freq[left_char] == 0:
                del char_freq[left_char]

            #move window forward
            window_start +=1

        max_length = max(max_length,window_end-window_start+1)
    return max_length

if __name__ == '__main__':
   print (longest_substring_after_replacement('aabccbb', 2))
   print(longest_substring_after_replacement('abbcb', 1))
   print(longest_substring_after_replacement('abccde',1))

