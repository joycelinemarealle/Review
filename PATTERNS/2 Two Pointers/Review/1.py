def pair_with_target_sum(nums, target_sum):
    #assume array is sorted
    #initialization
    left, right = 0, len(nums)-1

    #condition for pointers
    while left < right:
        #sum left + right numbers
        current_sum = nums[left] + nums[right]
        #compare sum to target
        if current_sum == target_sum:
            return [left,right]
        if current_sum > target_sum:
            #right pointer decreases
            right -=1
        else: #if sum , target the increae left pointer
            left+=1

    return [-1,-1] #if there is no pair with target sum then return

if __name__ == '__main__':
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))  # Output: [1.py, 3]