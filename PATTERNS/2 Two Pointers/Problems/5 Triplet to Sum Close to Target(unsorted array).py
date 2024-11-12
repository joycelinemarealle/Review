import math
def triplet_close_to_target(arr, target_sum):
    #sort the array
    arr.sort()
    smallest_difference = math.inf
    closest_sum = 0

    for i in range (len(arr)-2):
        left = i+1 #start at second element
        right = len(arr) -1 #right pointer index

        while (left < right):
            current_sum = arr[i] + arr[left] + arr[right]
            target_diff = target_sum - current_sum

            if target_diff == 0: #we found a triplet with exact sum
                return current_sum #sum of all numbers

            #the second part of following if is to handle the smallest sum when we have more than one solution
            if abs(target_diff) < abs(smallest_difference): #or abs(target_diff) == abs(smallest_difference):
                smallest_difference = target_diff

            if target_diff > 0:
                left +=1

            else:
                right -=1
    return target_sum -smallest_difference

if __name__ == '__main__':
    print(triplet_close_to_target([-2,0,1,2], 2))
    print(triplet_close_to_target([-3, -1, 1,2], 1))
