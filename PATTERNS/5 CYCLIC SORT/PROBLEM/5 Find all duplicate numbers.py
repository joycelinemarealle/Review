def find_all_duplicates(nums):
    # 1 Initialization
    i = 0

    # 2 Traverse through array
    while i < len(nums):
        # 3 Check if number at current index same as number at targe index. If not swap
        j = nums[i]-1
        if nums[i] != nums[j]:
            #Swap numbers
            nums[i], nums[j] = nums[j], nums[i] #swap
        else:
            i+=1

    duplicateNumbers = []
    #Traverse through swapped array to find duplicates.
    for i in range(len(nums)):
        if nums[i] != i +1:
            duplicateNumbers.append(nums[i])
    return duplicateNumbers

def main ():
    print (find_all_duplicates([3,4,4,5,5]))
    print(find_all_duplicates([5,4,7,2,3,5,3]))

main()