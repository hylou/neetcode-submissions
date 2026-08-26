class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # Calculate the time of car reaching the target
        queue = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        queue.sort(key=lambda x:x[0], reverse=True)

        # for each car from the first position, check if the later car can catch on
        res = 1
        first_car = queue[0]
        
        for car in queue[1:]:
            if first_car[1] < car[1]: # cannot catch
                first_car = car
                res += 1

        return res
