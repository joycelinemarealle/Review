def find_missing_numbers(nums):
    # 1 Initialization
    i = 0
    #2 Loop through array
    while i < len(nums):
        j = nums[i]-1
        #3 Swap if not at correct indices
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+=1
    #Empty array
    missing_nums =[]
    #4Loop through swapped array
    for i in range(len(nums)):
        #check if number at correct index if not add to array
        if nums[i] !=  i+1:
            missing_nums.append(i+1)
    # return array
    return missing_nums

def main():
    print(find_missing_numbers([2,3,1,8,2,3,5,1]))

main()

