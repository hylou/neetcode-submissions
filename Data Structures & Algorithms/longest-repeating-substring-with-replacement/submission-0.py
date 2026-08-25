class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        res = 0
        max_freq = 0
        count_map = defaultdict(int)
        left = 0

        for right, char in enumerate(s):
            count_map[char] += 1
            max_freq = max(max_freq, count_map[char])

            while (right - left + 1) - max_freq > k:
                count_map[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res

