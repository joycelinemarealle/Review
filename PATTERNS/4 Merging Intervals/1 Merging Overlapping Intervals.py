#create class Intervale

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_Interval(self):
        print("[" + str(self.start) + " , " + str(self.end) + "]",end='')

def merge(intervals):
    #Constaintif only one interview no need to merge
    if len(intervals) < 2:
        return intervals

    #sort intervals by start value to get least a.start
    intervals.sort(key = lambda x: x.start)

    #after sorting the first element is Interval least start value
    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end

    #loop through all intervals
    for i in range (1, len(intervals)): #starting from index 1 since saved index 0
        interval = intervals[i]
        #Check for overlapping . if current Interval start (b.start) < overlap <= previous Interval end (a.end)
        if interval.start <= end: #overlapping intervals so adjust the end
            end = max(interval.end, end)
        else:
            mergedIntervals.append(Interval(start,end)) #non overlapping Interval , add previous Interval and rest to current Interval
            start = interval.start
            end = interval.end

   #add the last Interval to store te non-overlapping intervals +final Interval after loop
    mergedIntervals.append(Interval(start,end))
    return mergedIntervals

def main ():
    print ("Merged intervals: ", end = '')
    for i in merge( [Interval(1,4), Interval(2,5), Interval(7,9)]):
        i.print_Interval()
    print()

    print ("Merged intervals: " , end = '')
    for i in merge ([Interval(6,7), Interval(2,4), Interval(5,9)]):
        i.print_Interval()
    print()

    print ("Merged intervals: ", end = '')
    for i in merge ( [Interval(1,4), Interval(2,6), Interval(3,5) ]):
        i.print_Interval()
    print()

main()