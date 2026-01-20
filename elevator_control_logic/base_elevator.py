from abc import ABC, abstractmethod

class BaseElevator(ABC):
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.total_time = 0
        self.movement_log = []

    @abstractmethod
    def move_to(self, target_floor):
        pass
