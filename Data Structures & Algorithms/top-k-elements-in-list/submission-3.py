class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        max_count = 0
        for key in count:
            max_count = max(max_count, count[key])
        buckets = [list() for _ in range(max_count)]
        for key in count:
            buckets[count[key]-1].append(key)
        result = list()
        for i in range(max_count-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
            if len(result) == k:
                return result
        return result