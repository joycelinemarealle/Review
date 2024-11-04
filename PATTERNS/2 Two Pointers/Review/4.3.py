#SORT ARRAY
# NO DUPLICATE ALLOWED  in the array of triples
# three numbers sum to zero
#Steps
#Sort array
# empty array,


#search triplets
#itierate through entire array
def search_triplets(arr):
    arr.sort() # Sort array;
    triplets = []
    target_sum = 0
    #Loop through entire array
    for i in range (len(arr)):
     # if i > 0 and not equal to i (not a duplicate )
     # compare the element with the sum of other pair of two
     # i += search_pair(arr, target_sum - i, i+1, triplets)
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_pair(arr,target_sum-arr[i], i+1, triplets)
    return triplets

#search pair(arr,target_sum_of_pair, left, triplets)
def search_pair(arr,target_sum_pair, left, triplets):
    #right =  len(arr)-1
    right = len(arr)-1
    # loop left < right
    while left < right:
        #compare current sum to the target_sum of pair. if matches found triplet
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum_pair:
            #add left and right to triplet array since need unique numbers
            triplets.append([-target_sum_pair,arr[left],arr[right]])
            # move left and right pointers since need unique triplets
            left +=1
            right +=1

            #if moved pointer and find duplicates skip
            while left < right and arr[left] == arr[left-1]:
                left +=1

            # if moved pointer and find duplicates skip
            while left < right and arr[left] == arr[left - 1]:
                right -=1
        #if current sum  < target   move pointer forward
        if current_sum < target_sum_pair:
            left +=1
        #if current sum > target sum of pair  move pointer backward
        else:
            right -=1
     #return triplets
    return triplets

if __name__ == '__main__':
    print(search_triplets([-3,0,1,2,-1,1,-2]))