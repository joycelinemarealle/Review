def cyclic_sort(nums):
    #1 Initialization
    i = 0

    #2 Loop through array
    while i < len(nums):
        # 3 Index calculation of number
        # index starts at zero so 3 will be at index 2
        j = nums[i] -1 #
        #4 Check if element is in right position
        if nums[i] != nums[j]: #comparenumbers at right position anf number at iteration
            # 5 Swap with number at the correct positions. Keep on swapping until number at iteration is at correct position
            nums[i], nums[j] = nums[j], nums[i]
        #6 if same then move to next value in array
        else:
            i+=1

    return nums


def main ():
    print ( cyclic_sort([3,1,5,4,2]))
    print(cyclic_sort([2,6,4,3,1,5]))

main()