class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        max_heap = list()
        temp_heap = list() # for storing those already removed items
        res = list()

        # create max heap
        for num in nums[:k]:
            heapq.heappush(max_heap, num * -1)

        res.append(max_heap[0] * -1)

        # iterate until the last
        idx_drop, idx_add = 0, k

        while idx_add < len(nums):
            num_drop = nums[idx_drop]
            num_add = nums[idx_add]

            # If num_drop = current max, just remove it
            if num_drop == max_heap[0] * -1:
                heapq.heappop(max_heap)
                # pop those stored numbers
                while temp_heap and max_heap[0] == temp_heap[0]:
                    heapq.heappop(max_heap)
                    heapq.heappop(temp_heap)
            # If not, you store the number, and remove them later
            else:
                heapq.heappush(temp_heap, num_drop * -1)

            # for num_add, just add them to the max_heap
            heapq.heappush(max_heap, num_add * -1)
            res.append(max_heap[0] * -1)

            # iterate
            idx_drop += 1
            idx_add += 1
            
        return res
        

