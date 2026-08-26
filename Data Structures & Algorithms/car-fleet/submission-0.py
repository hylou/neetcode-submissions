class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        queue = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)
        first_car = queue[0]
        res = 1
        
        def catch_up(target: int, car_front: Tuple[int], car_end: Tuple[int]):
            return car_end[1] > car_front[1] and \
            (target-car_front[0])*1.0/car_front[1] >= (target-car_end[0])*1.0/car_end[1]

        for car in queue[1:]:
            if not catch_up(target, first_car, car):
                first_car = car
                res += 1

        return res
