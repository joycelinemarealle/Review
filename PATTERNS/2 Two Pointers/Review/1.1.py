# [1,2,3,4,6]
# target = 6

def pair_with_target(arr,target):
    indices, left, right = [], 0, len(arr)-1
    #loop over array
    while left < right :
        total_sum = arr[left] + arr[right]

        if total_sum == target:
            return [left,right]

        if total_sum < target:
            left +=1
        else:
            right -=1
    return [-1,-1]
if __name__ == "__main__":
    print(pair_with_target([1,2,3,4,6], 6))

    # loop over array
    # compare the sum of arr[left] and arr[right] to target
    # if sum < target then move left pointer to right
    # if summ > target move right pointer to left
    # if sum == target then indice[left,right]
    #compare the sum of arr[left] and arr[right] to target
    #if sum < target then move left pointer to right
    #if summ > target move right pointer to left
    #if sum == target then indice[left,right]