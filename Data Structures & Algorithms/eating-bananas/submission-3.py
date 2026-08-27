class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hour_spent(k: int) -> int:
            res = 0
            for item in piles:
                res += (item-1)//k + 1
            return res

        if h == len(piles):
            return max(piles)

        left, right = 1, max(piles)

        while left < right:
            mid = (left+right) // 2
            total_hour = hour_spent(mid)
            if total_hour > h: # k to low
                left = mid + 1
            else: # total_hour <= h
                right = mid

        return left
        