class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        import heapq
        res_map = dict()
        intervals.sort(key=lambda x: (x[0], x[1]))
        minHeap = list()
        i = 0
        for q in sorted(queries):

            # Check interval until the q < left bound
            while i < len(intervals) and intervals[i][0] <= q:
                # for each interval, we store length. and right bound
                l, r = intervals[i]
                heapq.heappush(minHeap, (r-l+1, r))
                i += 1

            # Now we need to remove all intervals, until q <= right bound (within bound)
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            # Now the first item is the smallest interval
            res_map[q] = minHeap[0][0] if minHeap else -1

        return [res_map[q] for q in queries]
        