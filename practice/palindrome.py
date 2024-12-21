is_palindrome  = True

word = input ("Enter a word:" )
for i in range ( len(word)//2):
    if word[i] != word[-i-1]:
        is_palindrome = False
        break
    if is_palindrome:
        print("Palindrome")
    else:
        print("Not Palindrome")


