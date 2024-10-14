
def list_starting_indices_of_anagrams(str, pattern):
    #1 Initialization
    window_start, matched = 0,0
    char_freq = {}

    #2Track frequency of char in pattern
    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] +=1

    result_indices = [] #List to store starting indices

    #3Sliding window
    for window_end in range (len(str)):
        #4 check each character in str
        right_char = str[window_end]
        if right_char in char_freq:
            char_freq[right_char] -=1 #decrement freq if char in window in hashmap
            if char_freq[right_char] == 0: #if freq zero then complete match
                matched +=1

        #5 Check if valid anagram
        if matched == len(pattern) :
            result_indices.append(window_start)#return list of starting indices
    #6 shrink window
        if window_end >= len(pattern) -1: #(window_start-window_end+1 >= len(pattern)
            left_char= str[window_start]
            window_start +=1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -=1 #before putting character bac, decrement the matched count
                char_freq[left_char] +=1
    return result_indices

if __name__ == '__main__':
    print(list_starting_indices_of_anagrams("ppqp", "pq"))
