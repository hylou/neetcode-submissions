class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]: # sill at right
                l = mid + 1
            else:
                r = mid # may or may not be mimunin, cannot do -1
        return nums[l]


        