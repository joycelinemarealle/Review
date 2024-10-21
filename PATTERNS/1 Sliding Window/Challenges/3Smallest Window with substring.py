import math
def smallest_length_with_substring(str, pattern):
    #1.py Initialization
    window_start, matched, substr_start  = 0,0,0
    min_length = len(str) +1
    char_freq = {}

    #2 Hashmap of pattern
    for char in pattern:
        if char not in char_freq:
            char_freq[char] =1
        else:
            char_freq[char] +=1

    #3 Slide window
    for window_end in range (len(str)):
         #4 go through each character in window to see if present in hashmap
        right_char = str[window_end]
        if right_char in char_freq:
            char_freq[right_char]-=1 #reduce frequency of it
            if char_freq[right_char] >= 0: #count every instance of character if also in hashmap
                matched +=1
        #5 Shrink window when matched all characters (matched == ln(pattern)
        while matched == len(pattern):
            if min_length > (window_end-window_start+1 ):
                min_length = window_end-window_start+1
            substr_start = window_start #track beginning of matched substring

            left_char = str[window_start]
            window_start +=1
            if left_char in char_freq:
                #can have redundant character
                #count when useful occurrence of a matched character
                if char_freq[left_char] ==0:
                    matched -=1 #re-adjust back the matched by -1.py so that rest as slide window
                char_freq[left_char] +=1
    #return smallest substring
    if min_length > len(str):
        return ""
    return str[substr_start: substr_start+ min_length] #exclusive of right boundary


if __name__ == '__main__':
    print(smallest_length_with_substring("aabdec", 'abc'))
#Notes

# 1.py Initialization
# window_start, max_length, matched, hashmap

# 2 hashmap of pattern

# 3 slide window

# 4 go through each character in window to see if present in hashmap

# 5 UNTIL MATCHED REACHED

# 6 Track max length of window

# 7 sHRINK window when size of window >= len of pattern

# return max_length