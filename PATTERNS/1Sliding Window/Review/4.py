def longest_substring_with_distinct_characters(str,k):
    #1 Initialization
    window_start = 0
    max_length = 0
    char_freq = {}
    #2 Slide window
    for window_end in range (len(str)):
        right_char = str[window_end]

        # 3 Fill in hashmap
        if right_char not in char_freq:
                char_freq[right_char] = 1
        else:
             char_freq[right_char] += 1

        #4 Shrink window size when > the K distinct Char
        while len(char_freq) > k:
            left_str = str[window_start]
            #5 re-balance hashmap
            char_freq[left_str] -=1

            if char_freq[left_str] == 0: #if zero then remove
                del char_freq[left_str]

            #6 move ahead
            window_start +=1

            # 8 max_length = max(max_length,window_end -window_start+1)
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

if __name__ == '__main__':
    print (longest_substring_with_distinct_characters("araaci",2))