#str = string array with letters
#k number of distinct no
def longest_substring_with_k_distinct(str,k):
    window_start = 0
    max_length = 0
    char_frequency = {} #empty dictionary to hold key value

    #Slide through the str array
    for window_end in range (len(str)):
        right_char = str[window_end]

        if right_char not in char_frequency:
            char_frequency[right_char] = 0
            #if character exists already
        else:
            char_frequency[right_char] +=1

        while len(cj)
        #do something
    #if more than k:
    #track lenght