def insert(intervals, new_interval):
    #1 initialization
    merged = []
    i,start,end = 0,0,1

    #2skip all intervals which end before new interval
    #add intervals before the new interval
    #i < len(intervals see if within range of indices
    #intervals[i][end] end of current interval
    while i< len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i=+1

    #3 Merge overlapping intervals
    while i < len(intervals) and intervals[i][start] < new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i+=1

    #4  Add merged interval
    merged.append(new_interval)

    #5 Add remaining intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i+=1

    #6 return result
    return merged

def main():
    print("Intervals after inserting the new interval: " + str(insert([[1,3], [5,7],[8,12]], [4,6])))
    print("Intervals after inserting the new interval: " + str(insert([[1,3],[5,7]], [1,4])))
main ()