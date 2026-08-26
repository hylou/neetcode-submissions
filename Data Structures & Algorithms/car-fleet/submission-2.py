class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Calculate the time of car reaching the target
        queue = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        queue.sort(key=lambda x:x[0], reverse=True)

        # for each car from the first position, check if the later car can catch on
        res = 1
        first_car_index = 0
        
        for idx in range(1, len(position)):
            if queue[first_car_index][1] < queue[idx][1]: # cannot catch
                first_car_index = idx
                res += 1

        return res
