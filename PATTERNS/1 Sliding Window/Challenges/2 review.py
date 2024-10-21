def list_of_anagram(str , pattern):
    window_start = 0
    matched = 0
    char_freq = {}

    for char in pattern:
        if char not in char_freq:
            char_freq[char] =1
        else:
            char_freq[char] +=1

    results_indices = []

    for window_end in range ( len(str)):
        right_char = str[window_end]

        if right_char in char_freq:
            char_freq[right_char] -=1

            if char_freq[right_char] ==0:
                matched +=1

        if matched == len(pattern):
            results_indices.append(window_start)


        if window_end >= len(pattern)  -1:
            left_char = str[window_start]
            window_start +=1

            if left_char in char_freq:
               if  char_freq[left_char] == 0:
                   matched -=1
               char_freq[left_char] +=1

    return results_indices


if __name__ == '__main__':
    print(list_of_anagram("ppqp", "pq"))
