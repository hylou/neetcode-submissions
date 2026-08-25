class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        results = [1] * len(nums)

        # from left
        for i in range(1, len(nums)):
            results[i] = results[i-1] * nums[i-1]

        # from right
        cur = 1
        for i in range(len(nums)-2, -1, -1):
            cur *= nums[i+1]
            results[i] *= cur

        return results

