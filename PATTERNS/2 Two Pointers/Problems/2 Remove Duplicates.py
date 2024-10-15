def remove_duplicates(arr):
    #index of next non-duplicate element
    next_non_duplicate = 1

    #one pointer iterates over the entire array
    i = 1 #next one
    while i < len(arr):
        if arr[next_non_duplicate-1] != arr[i]: #if previous number not equal to next number
            arr[next_non_duplicate] == arr[i]
            next_non_duplicate+=1
        i+=1
    return next_non_duplicate

if __name__ == '__main__':
    print(remove_duplicates([2,3,3,6,9,9]))