class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_map = dict()
        result = list()
        for word in strs:
            char_map = [0] * 26
            for char in word:
                char_map[ord(char) - ord('a')] += 1
            char_map_key = tuple(char_map)
            if char_map_key not in word_map:
                word_map[char_map_key] = [word]
            else:
                word_map[char_map_key].append(word)
        for key in word_map:
            result.append(word_map[key])
        return result
            
