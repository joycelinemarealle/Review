def fruits_in_basket(fruits):
    #1 Initialization
    window_start = 0
    max_length = 0
    fruit_freq= {} #empty dictionary to hold frequency of values in each window

    #2 sliding window
    for window_end in range (len(fruits)):
        #3Check each fruit in array
        right_fruit = fruits[window_end]

        #check in dictionary
        if right_fruit not in  fruit_freq:
            fruit_freq[right_fruit] = 1
        else:
            fruit_freq[right_fruit] +=1

        #4 Shrink the window when dictionary length> distinct length
        while len(fruit_freq) > 2:
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -=1 #shrink window
            if fruit_freq[left_fruit] == 0: #no longer in window
                del fruit_freq[left_fruit]
            window_start +=1 #slide window ahead
        #5 Track maximum length of the valid window
        max_length = max(max_length, (window_end-window_start+1))
    return max_length

if __name__ == '__main__':
    fruits = ['A', 'B', 'C', 'A', 'C']
    print(fruits_in_basket(fruits))