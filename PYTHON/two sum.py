#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
#Example 1.py:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1.py]
#Explanation: Because nums[0] + nums[1.py] == 9, we return [0, 1.py].

def two_sum(nums,target):
    num_to_index = {}

    #create hashmap to store diff between target and  num
    for i, num in enumerate(nums):
        #calculate the required number to reach target
         complement = target - num

        #check if complement in the dictionary
         if complement in num_to_index:
            return [num_to_index[complement], i]

    #store current number and its index in hashmap
    num_to_index[num] = i

    #if no solution found
    return None



