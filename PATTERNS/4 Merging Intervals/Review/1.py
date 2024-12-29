#2-5 & 3-7 -> 1-7
#merge interval
#overlapping
#a is interval with least start value and b is the interval as you iterate through list of intervals
#sort intervals such that a.start < = b.start
#if overlapp( b.start < a.end) then new interval c
    #c.start = a.start
    #c.end = max(a.end, b.end)

#if not :
    #store into mergedlist into start and end of previous interval
    #reset new start and end for current interval

#add the last start and end to the merged list

#return merged list

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end

    def print_interval(self):
        print ("[ " + str(self.start) + ", " + str(self.end) + "]", end = ' ')


def merge(intervals):


    # constaint if only one interval return it no need to merge
    if len(intervals) < 2:
        return intervals
    #Sort list of intervals
    intervals.sort(key = lambda x:x.start)

    #save the first interval in the intervals list
    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    #iterate through the list of intervals and
    for i in range ( 1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end: #overlapping b overlaps a
            end = max(interval.end,end)

        else: #no overlapping so save previous interval
            merged_intervals.append(Interval(start,end))
            #reset start and end with current interval
            start = interval.start
            end = interval.end

    #add last interval to mergedintervals list
    merged_intervals.append(Interval(start,end))
    return merged_intervals

def main ():
    print("Merged Intervals : ")
    for i in merge([Interval(1,4), Interval(2,5), Interval(7,9)]):
        i.print_interval()
    print()

    print("Merged Intervals: ")
    for i in merge([Interval(6,7), Interval(2,4), Interval(8,9)]):
        i.print_interval()
    print()

main()