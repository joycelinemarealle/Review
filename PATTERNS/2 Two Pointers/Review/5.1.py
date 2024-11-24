import math
def triplets_close_to_target(arr, target_sum):
    arr.sort()
    smallest_difference = math.inf

    for i in range (len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while (left < right):

            current_sum = arr[i] + arr[left] + arr[right]
            target_diff = target_sum - current_sum
           # min_difference = min (target_diff, smallest_difference)

            if target_diff == 0:
                return target_sum - target_diff

            if abs(target_diff) < abs(smallest_difference):
                smallest_difference = target_diff #assign new minimum

            elif current_sum < target_sum:
                left +=1

            else:
                right -=1

        return target_sum - smallest_difference



if __name__ == '__main__':
    print(triplets_close_to_target([-2,0,1,2], 2))
    print(triplets_close_to_target([-3, -1, 1,2], 1))
#sort array
#loop i upto 2 less thna length of arr
#left i+1 right lrn(srr)-1, smallest_difference
#track current sum fo triplets and compare to target
#see which triplet has the least difference
#move pointers depending on if current sum, > or <  target sum
#Return sum of triple with least difference