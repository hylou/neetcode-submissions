class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0

        left_max = [height[0]] * len(height)


        # calculate max from left
        for i in range(1, len(height)):
            left_max[i] = max(height[i], left_max[i-1])
        # calculate max from right, and calculate trapped water
        right_max = height[len(height)-1]
        res += max(0, min(right_max, left_max[len(height)-1]) - height[len(height)-1])
        for j in range(len(height)-2, -1, -1):
            right_max = max(right_max, height[j])
            res += max(0, min(right_max, left_max[j]) - height[j])
        return res
        