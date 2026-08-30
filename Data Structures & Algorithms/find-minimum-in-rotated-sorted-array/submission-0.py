class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1
        
        if nums[l] < nums[r]:
            return nums[l] # no rotation

        else: # has rotation
            while l < r:
                mid = (l+r) // 2
                if nums[l] < nums[r]:
                    return nums[l]
                elif nums[mid] >= nums[l]:
                    l = mid + 1
                else:
                    r = mid
        return nums[r]


        