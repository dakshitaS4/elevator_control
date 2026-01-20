# def move_elevator(current_floor, target_floor):
#     path = []

#     while current_floor < target_floor:
#         current_floor += 1
#         path.append(current_floor)

#     return path



# class Elevator:
#     def __init__(self, current_floor):
#         self.current_floor = current_floor
#         self.total_time = 0
#         self.movement_log = []

#     def move_to(self, target_floor):
#         # Move UP
#         while self.current_floor < target_floor:
#             self.current_floor += 1
#             self.movement_log.append(self.current_floor)
#             self.total_time += 1

#         while self.current_floor > target_floor:
#             self.current_floor -= 1
#             self.movement_log.append(self.current_floor)
#             self.total_time += 1



from base_elevator import BaseElevator

class Elevator(BaseElevator):
    def move_to(self, target_floor):
        while self.current_floor < target_floor:
            self.current_floor += 1
            self.movement_log.append(self.current_floor)
            self.total_time += 1

        while self.current_floor > target_floor:
            self.current_floor -= 1
            self.movement_log.append(self.current_floor)
            self.total_time += 1


class HighSpeedElevator(BaseElevator):
    def move_to(self, target_floor):
        distance = abs(target_floor - self.current_floor)
        self.current_floor = target_floor
        self.movement_log.append(self.current_floor)
        self.total_time += max(1, distance // 2)
