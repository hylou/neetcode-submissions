class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]: # rotate point is at right
                if nums[mid] < target or target < nums[l]:
                    l = mid + 1 # means the target is at right
                else:
                    r = mid - 1 # means the target is at left
            else: # rotate point is at left
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 # means the target is at right
                else:
                    l = mid + 1
        return -1
        