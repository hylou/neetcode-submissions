class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = list()
        for word in strs:
            encoded.extend([str(len(word)), '#', word])
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = list()
        cur = 0

        while cur < len(s):
            # read until find '#'
            cur_hashtag = cur
            while s[cur_hashtag] != '#':
                cur_hashtag += 1
            length = int(s[cur:cur_hashtag])
            cur = cur_hashtag + 1 # currently cur_hashtag is at the "#"

            # get the decoded word
            decoded.append(s[cur:cur+length])

            cur += length
        
        return decoded


