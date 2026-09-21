class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use min heap
        h = list()

        # puth only k items
        for i in range(k):
            heapq.heappush(h, nums[i])

        kth = heapq.heappop(h) # get the smallest (current kth largest)

        for num in nums[k:]:
            if num <= kth:
                continue
            else:
                kth = heapq.heappushpop(h, num)
        
        return kth
        