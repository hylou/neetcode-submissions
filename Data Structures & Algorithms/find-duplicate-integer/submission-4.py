class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd’s Fast & Slow Pointer (need to study)
        slow, fast = 0, 0

        while True: # must start with the first step
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow