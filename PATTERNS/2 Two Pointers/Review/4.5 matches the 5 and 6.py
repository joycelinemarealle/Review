
def search_triplets(arr):
    arr.sort()
    triplets =[]
    for i in range (len(arr) -2):
        if i >0 and arr[i] == arr[i-1]:
            continue
        right = len(arr) - 1
        left = i + 1
        target_sum = arr[i]

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target_sum:
                triplets.append([-target_sum, arr[left], arr[right]])
                left +=1
                right -=1

                while left < right and arr[left] == arr[left-1]:
                    left+=1

                while left<right and arr[right] == arr[right+1]:
                    right -=1
            elif current_sum > target_sum:
                right -=1

            else:
                left+=1

    return triplets


if __name__ == '__main__'  :
    print(search_triplets([-3,0,1,2,-1,1,-2]))

#sort for the duplicates to be next to each other
#search triplet iteratre through array, skip duplicates
#search pair whose sum equals to target, move left pointer+ right , skip duplicates
#if not equal then move pointers
#return triplets array