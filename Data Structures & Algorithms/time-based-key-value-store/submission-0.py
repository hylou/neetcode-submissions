from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if len(self.dictionary[key]) == 0 or timestamp < self.dictionary[key][0][1]:
            return ""

        l, r = 0, len(self.dictionary[key]) - 1

        while l < r:
            mid = (l+r+1)//2 # lean to the right to avoid inifinate loop
            if timestamp < self.dictionary[key][mid][1]:
                r = mid - 1
            else:
                l = mid
        return self.dictionary[key][l][0]
        
