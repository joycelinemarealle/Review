#[2,3,3,3,6,9,9] [2,3,6,9]

def remove_duplicates(arr):
    next_non_duplicate = 1
    i = 1
    while i < len(arr):
        if arr[next_non_duplicate-1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate +=1
        i+=1

    return next_non_duplicate

if __name__ == '__main__':
    print(remove_duplicates([2,3,3,6,9,9]))



#first pointer to itierate through array
#second pointer splace the next non duplicate
#compare numbers pointed at by these pointer. if arr[right] == larr[eft] then then the number is put in next non duplicatevalu =e of new array
#if dame then skip right +1
