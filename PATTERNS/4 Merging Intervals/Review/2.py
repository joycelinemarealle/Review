def insert(intervals, new_interval):
    merged_intervals = []
    # 1 initialization
    i,start,end = 0,0,1
    merged_list = [] //
    #2 Skip all intervals that come before new interval and add them to new merged list
    while i< len(intervals) and intervals[i][end] < new_interval[start]:
        #new interval overlapping
       merged_intervals.append(intervals[i])
       i+=1

    #3 Merge all intervals that overlap with new_interval
    while i< len(intervals) and intervals[i][start] <= new_interval[end]:
        #adjust start and end interval
        new_interval[start] = min (intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i+=1

    #4 add merged new_interval
    merged_intervals.append(new_interval)

    #5 add all remaining intervals to output
    while i < len(intervals):
        merged_intervals.append(intervals[i])
        i +=1
    return merged_intervals



    return merged_intervals

def main ():
    print("The new intervals after inserting new interval is : "+ str(insert([ [1,3], [5,7], [8,12] ],[4,6])))

main()

# non-overlapping intervals + sorted -> insert new interval at correct position  + merge rest of intervals mutually exclusive
# input is alist
# output is a list

# 1-3 , 4-5 ,6-7, ***  8-9, 10- 12 -> new :  9-11

# where to insert interval?
# a = new interval b = interval in iteration
# skipp all intervals that come before new interval (b.end < a.start)
# once i am in correct index
# merge overlapping intervals with new interval
# c. start = min(a.start, b.start)
# c. end = max( a.end, b,end)

# add new interval  interval to mergef list
#add remaining intervals
# return merged list