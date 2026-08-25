class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        length = dict()
        result = 0
        for num in nums:
            if num in length.keys():
                result = max(result, length[num])
                continue
            cur_length = 1
            cur = num + 1
            while cur in num_set:
                cur_length += 1
                cur += 1
            result = max(result, cur_length)
            # cache intermediate results
            for i in range(cur_length):
                length[num+i] = cur_length-i
        return result
            
                

        