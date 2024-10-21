def longest_substring_no_repeating_characters(str):
    #1.py Initialization
    window_start = 0
    max_length = 0
    char_freq = {}

    # 2 Slide window
    for window_end in range (len(str)):
        # 3 Go for each character to fill in hashmap
        right_char = str[window_end]

        if right_char not in char_freq:
            char_freq[right_char] = 1
        else:
            char_freq[right_char] +=1

        #4 Shrink window once characters repeats
        while char_freq[right_char] >1:
            left_char = str[window_start]
            #Rebalance hashmap
            char_freq[left_char] -=1

            if char_freq[left_char] == 0:
                del char_freq[left_char]
            #move left element ahead
            window_start +=1
        #Track max length
        max_length = max(max_length, window_end-window_start+1)
    return max_length

if __name__ == "__main__":
    print(longest_substring_no_repeating_characters("aabccbb"))
    print(longest_substring_no_repeating_characters("abbbb"))
    print(longest_substring_no_repeating_characters("abccde"))




