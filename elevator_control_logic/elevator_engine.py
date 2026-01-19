# def move_elevator(current_floor, target_floor):
#     path = []

#     while current_floor < target_floor:
#         current_floor += 1
#         path.append(current_floor)

#     return path



class Elevator:
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.total_time = 0
        self.movement_log = []

    def move_to(self, target_floor):
        # Move UP
        while self.current_floor < target_floor:
            self.current_floor += 1
            self.movement_log.append(self.current_floor)
            self.total_time += 1

        # Move DOWN (important for correctness)
        while self.current_floor > target_floor:
            self.current_floor -= 1
            self.movement_log.append(self.current_floor)
            self.total_time += 1
