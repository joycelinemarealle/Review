def max_fruits_in_basket(fruits):
    #1.py Initialization
    window_start = 0
    max_length = 0
    fruit_freq = {}

    #2 Slide window in range of fruits
    for window_end in range (len(fruits)):
        #3 Process each fruit to fill in hashmap
        right_fruit = fruits[window_end]

        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 1
        else:
            fruit_freq[right_fruit] +=1

        #Shrink whenever len of hashmap > 2
        while len(fruit_freq) >2:
            #Re-balance hashmap when left element goes out
            left_char = fruits[window_start]
            fruit_freq[left_char] -=1
            if fruit_freq[left_char] == 0:
                del fruit_freq[left_char]
           #move window ahead
            window_start+=1

        #Track max lenght
        max_length = max (max_length, window_end-window_start+1)
    return max_length
if __name__ == '__main__':
    fruits = ['A', 'B', 'C', 'A', 'C']
    print(max_fruits_in_basket(fruits))
