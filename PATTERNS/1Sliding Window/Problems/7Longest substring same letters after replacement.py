
def length_longest_substring(str,k):
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

        #track frequency of each character
        max_repeat_letter_count = max(max_repeat_letter_count, char_freq[right_char])

        #4 Shrink window when remaining characters > k since can't replace more than k characters
        #window can have a character repeated tha 'max_repeat_letter_count' then rest of characters in window replaced
        if ( window_end -window_start +1 - max_repeat_letter_count) > k:
           left_char = str[window_start]
           char_freq[left_char] -= 1 # reduce count of character
           window_start +=1 #move window ahead

        #5 Track max_length of window
        max_length =  max(max_length, window_end-window_start +1)
    return max_length

if __name__ == '__main__':
   print (length_longest_substring('aabccbb', 2))
   print(length_longest_substring('abbcb', 1))
   print(length_longest_substring('abccde',1))