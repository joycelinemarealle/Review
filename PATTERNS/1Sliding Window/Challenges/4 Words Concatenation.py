def find_words_concatenation(str, words):
    # if words array is empty return empty [
    if len(words) == 0 or len(words[0]) == 0:
        return []
    # 1Keep the frequency of every word in a HashMap
    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    # 2 Starting from index in the string, try matching all words
    result_indices = []  # to hold indices with substring holding all 2 words
    words_count = len(words)  # 2 words in array cat, fox
    word_length = len(words[0])  # 3 char per word

    #range of i goes through catfox, foxcat,catfox. So len of entire str -(size of given words combined)
    for i in range(len(str) - (words_count * word_length) +1):
        words_seen = {}
        for j in range (0,words_count):
            next_word_index = i+j*word_length
            #Get the next word from string
            word = str[next_word_index:next_word_index +word_length]

            if word not in word_frequency: #Break if we do not see
                break
            #3 in each iteration keep track of all words we have already seen in another hashmap
            #Add the word to the words_seen map
            if word not in words_seen:
                words_seen[word] =1
            else:
                words_seen[word] +=1
            #4 if word not  found or greater than frequency go to next character in string
            #No need to further process if word higher freq than required
            if words_seen[word] > word_frequency.get(word,0):
                break
            #5 store index if we have found ALL WORDS
            if j+1 == words_count:
                result_indices.append(i)
    return result_indices

if __name__ == "__main__":
    print(find_words_concatenation("catfoxcat", ["cat", "fox"]))