class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res = 0
        left_cur = 0
        idx_map = {}

        for i, char in enumerate(s):
            if char in idx_map:
                left_cur = max(left_cur, idx_map[char] + 1) # whether to move the cursor forward
            idx_map[char] = i
            res = max(res, i - left_cur + 1) # calculate current string length
        
        return res

        