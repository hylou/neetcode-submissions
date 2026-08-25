class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = list()
        nums.sort()

        for i in range(len(nums)-2):
            if nums[i] > 0:
                return res
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, len(nums)-1
            while j < k:
                three_sum = nums[i]+ nums[j] + nums[k]
                if three_sum < 0:
                    j += 1
                elif three_sum > 0:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # remove duplicate
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res



