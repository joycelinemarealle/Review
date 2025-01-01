def find_missing_number(nums):
    # 0 -> n meaning 0 is at index 0 num[i] = i
    #1 Initialization of values
    i, n= 0,len(nums)

    #2 Loop through array
    while i < n:
        j = nums[i]
        # 3 Find if number at correct position
        #ignore the n since cannot place it in array hence num[i] < nums.length
        #indices go from 0, n-1
        #SWAP values with valid indices num has to be less than number of elements. eg 7 cannnot be swapped in 4 sized array
        if nums[i] < n and nums[i]!= nums[j]:
            #4 Swap numbers to correct place
            nums[i],nums[j] = nums[j], nums[i]
        else:
            i+=1

    #5 Find the first number missing from its index, that will be our missing number
    for i in range(n):
        if nums[i] != i:
            return i #if loop finds a mismatch, return i, i first missing number

    return n #no mismatch found then return n since will be missing number. All numbers from 0-n-` are present

def main():
    print(find_missing_number([4,0,3,1]))


main()