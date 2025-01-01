def find_duplicate(nums):
    # 1 Initialization
    i = 0

    # 2 Loop through array
    while i < len(nums):
        # 3 Check if number at its correct position first eg num[0] == 0+1 so it is. increment i to 1
        if nums[i] != i +1:
            # Swap
            j = nums[i]-1
            #Check if number at current index is diff that on target index. If same no need to swap
            if nums[i] != nums[j]:
                nums[i],nums[j] = nums[j], nums[i]
            else: #we have duplicate since both current number at index i and target index have same value
                return nums[i]
        else:
            i+=1
    return -1

def main():
    print(find_duplicate([1,4,4,3,2]))
    print(find_duplicate([2,1,3,3,5,4]))

main()