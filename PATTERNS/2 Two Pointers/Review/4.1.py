# sort array
# method skip duplicates and call search pair method
# search pair
# left, right , target


def search_triplets(nums):
    nums.sort()
    triplets = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        search_pair(nums, -nums[i], i + 1, triplets)
    return triplets


def search_pair(nums, target, left, triplets):
    right = len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        # found triplet
        if current_sum == target:
            triplets.append([-target, nums[left], nums[right]])  # add it to the array

            left += 1  # move ahead since need unique
            right -= 1  # move backward since need unique
            while left < right and nums[left] == nums[left - 1]:  # ensures the triplets are unique
                left += 1
            while left < right and nums[right] == nums[right+1]:  # ensures the triplets are unique
                right -= 1
        elif current_sum > target:
            left += 1

        else:
            right -= 1
if __name__ == '__main__':
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
