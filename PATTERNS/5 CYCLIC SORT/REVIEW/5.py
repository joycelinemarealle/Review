# 1 -> n
# find duplicate numbers without extra space

# Loop through the array
#check number at iteration is smae as number at target
  # if not  same then swap
  #
#loop throug swapped array
    #if value not at correct index then it is a duplicat

def find_all_duplicate_numbers(nums):
    # 1 initialization
     i =0
     while i < len(nums):
        j = nums[i] -1
        # 2 Swap if number at current index is not the same as number at target index
        if nums[i] != nums[j]:
             #swap
            nums[i], nums[j] = nums[j], nums[i]
        else:
             i+=1

     duplicates = []

     #Loop through swapped array  #if number not at correct index then duplicate
     for i in range (len(nums)):
         if nums[i] != i+1:
             duplicates.append(nums[i])
     return duplicates


def main ():
    print ( find_all_duplicate_numbers([3,4,4,5,5]))

main ()