class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_products = 1
        zeros = 0
        results = [0] * len(nums)
        for num in nums:
            if num != 0:
                all_products *= num
            else:
                zeros += 1
        
        if zeros >= 2:
            return results

        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    results[i] = all_products
                elif zeros > 0:
                    results[i] = 0
                else:
                    results[i] = all_products//nums[i]

        return results

