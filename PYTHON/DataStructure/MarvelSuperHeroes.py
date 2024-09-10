heroes = [ "spider man", "thor", "hulk", "iron man", "captain america"]


#1. Length of the list
print("Length of heroes list is ", len(heroes))

#2. Add 'black panther' at the end of this list
heroes.append(" black panther")

#3. You realize that you need to add 'black panther' after 'hulk',# so remove it from the list first and then add it after 'hulk'
heroes.pop(5)
heroes.insert(3,"black panther")
print("New Heroes list ",heroes)


#4. Now you don't like thor and hulk because they get angry easily :)
    # So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
    # Do that with one line of code.
heroes [1:3] =["doctor strange"]
print("New heroes list with doctor strange", heroes)

#5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print("Sorted heroes alphabetically",heroes)

