#sort array
import math
def triplets_close_to_target(arr, target_sum):
    arr.sort()
    smallest_diff = math.inf

    #loop through the array
    for i in range (len(arr)-2):
        left = i +1
        right = len(arr)-1

        #compare current sum to target_sum
        while (left < right):
            current_sum = arr[i]+ arr[left] + arr[right]
            target_diff = target_sum - current_sum

            #compare difference between sums
            if target_diff == 0: #we found the triplet with exact target sum
                return current_sum

            #if multiple smallest sum return smallest
            if abs(target_diff) < abs(smallest_diff): #or abs(target_diff) == abs(smallest_diff):
                smallest_diff = target_diff

            if current_sum < target_sum:
                left +=1 # need triplet with bigger sum
            else:
                right -=1 #need triplet with smaller sum
    return target_sum- smallest_diff #the actual sum of numbers

if __name__ == '__main__':
    print(triplets_close_to_target([-2,0,1,2], 2))
    print(triplets_close_to_target([-3, -1, 1,2], 1))
