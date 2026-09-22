class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Total time = len(tasks) + idle time
        # bucketizing
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort(reverse=True) # decending

        maxf = count[0]
        idle = (maxf-1) * n

        for num in count[1:]:
            idle -= min(maxf-1, num)

        return max(0, idle) + len(tasks)

        