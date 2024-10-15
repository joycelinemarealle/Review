def pair_with_target_sum(arr, target_sum):
    # Initialization of two pointers
    left, right = 0, len(arr) - 1  # left starts from the beginning, right starts from the end

    # While loop to move the pointers
    while left < right:
        # Calculate the sum of the values at the left and right pointers
        current_sum = arr[left] + arr[right]

        # If the current sum matches the target sum, return the pair of indices
        if current_sum == target_sum:
            return [left, right]

        # If the current sum is greater than the target sum, move the right pointer to the left
        if current_sum > target_sum:
            right -= 1
        else:  # If the current sum is less than the target sum, move the left pointer to the right
            left += 1

    # If no pair is found, return [-1, -1]
    return [-1, -1]

# Example usage
if __name__ == '__main__':
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))  # Output: [1, 3]