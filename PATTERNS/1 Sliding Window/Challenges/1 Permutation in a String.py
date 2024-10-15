def find_permutation(str, pattern):
    #1.py initialization
    window_start, matched = 0, 0
    char_freq = {}

    #Track frequencies of char in pattern
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] +=1
    #Match all characters in char_freq dictionaries with the current window
    #Sliding window
    for window_end in range (len(str)):
        #3 Go through each character in str array to see if exist in char_freq
        right_char = str[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1 #if exist decrease the frequency of matched character
            if char_freq[right_char] == 0: #freq zero then complete match
                matched +=1
        if matched == len(char_freq): #check if pattern length met
            return True

        #4 Shrink window #if pattern
        if window_end >= len(pattern) -1: #window stars from zero so len-1.py
            left_char = str[window_start]
            window_start += 1

            #re-adjust the hashmap when element through out. reverse of right_char
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -=1
                char_freq[left_char] +=1
    return False

if __name__ == '__main__':
    print(find_permutation("oidbcaf", "abc"))

