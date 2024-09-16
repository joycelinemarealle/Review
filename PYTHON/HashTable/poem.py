# Contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in python and print every word and its count as show below.
# Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.

# Use a Hash table -Dictionaries since need key-value pair

# open file
# for line split by space
# word captured in dictionary
# work as key
# count value


words_Dict = {}
count_of_each_word = 0
index = 0
with open('poem.txt', 'r') as csvfile:
    for line in csvfile:
        words = line.split(' ')  # split by space to get words
        for word in words:
            word = word.replace('\n','')
            word = word.replace(',', '')
            if word in words_Dict:
                words_Dict[word] += 1
            else:
                words_Dict[word] = 1
print(words_Dict)

# OR#
# words_array = []
# with open ('poem.txt', 'r') as csvfile:
#     for line in csvfile:
#         word = line.split(' ') #split by space to get words
#         words_array.append(word)
# print(words_array)
