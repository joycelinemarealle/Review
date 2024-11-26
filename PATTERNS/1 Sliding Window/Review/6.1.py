# def longest_substring_withK_distinct_char(arr,k):
#     max_length = 0
#     window_left = 0
#     char_freq = {}
#     count_char= 0
#
#     for window_right in range (len(arr)):
#         #check if present in hashmap
#         if arr[window_right] in char_freq:
#             count_char+=1
#
#         if  char_freq <= k:
#             window_size = window_left - window_right +1
#             max_length =   max (max_length, window_size)
#
#             #reduce count of elemet thrown out the window
#             char_freq[arr[[window_left]] ]-=1
#             if char_freq[arr[[window_left]] == 0:
#                 del char_freq[arr[window_left]]
#             window_left +=1
#
#     return max_length
#





#keep track of unique element as key and counts as value . so hashmap
#iterate through a array
    #check of in hashmap if yest increase count
# #sliding window from element
        # keep track of unique element as key and counts as value
        #reduce the window if
            #if value of keys <= k:
            #track max length of windoq wise
            #throw element so if it is in reduce its count
                 #if count zero then the value = 0
            #window_left forwaed
