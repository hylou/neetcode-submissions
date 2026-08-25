class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if len(t) > len(s) or t == "":
            return ""

        target_counter = Counter(t)
        current_counter = Counter()

        res_index = [-1, -1]
        res_length = float("infinity")
        char_match, char_need = 0, len(target_counter) # distinct chars here
        l = 0

        for r in range(len(s)):

            # add char to current counter
            current_char = s[r]
            current_counter[current_char] += 1

            # check if the char count meet the need
            if current_char in target_counter and \
            target_counter[current_char] == current_counter[current_char]:
                char_match += 1

            # if all chars are meet, shrink the window
            while char_match == char_need:
                # check if need to update res boundary
                if (r - l + 1) < res_length:
                    res_index = [l, r]
                    res_length = r - l + 1
                
                # remove the first char, and move cursor l
                first_char = s[l]
                current_counter[first_char] -= 1

                if first_char in target_counter and \
                target_counter[first_char] > current_counter[first_char]:
                    char_match -= 1
                l += 1
        
        # output result
        l, r = res_index
        return s[l:r+1] if res_length != float("infinity") else ""
            




        
        