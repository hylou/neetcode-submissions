class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        if len(s1) > len(s2):
            return False
        key_counter = Counter(s1)
        value_counter = Counter(s2[:len(s1)])
        l, r = 0, len(s1)
        while r < len(s2):
            if key_counter == value_counter:
                return True
            value_counter[s2[l]] -= 1
            value_counter[s2[r]] += 1
            l += 1
            r += 1

        return key_counter == value_counter
            