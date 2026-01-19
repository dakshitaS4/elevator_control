from input_handler import input_handler
from request_manager import manage_requests
from elevator_engine import move_elevator
from time_calculator import calculate_time


def elevator_controller():
    MIN_FLOOR = 1
    MAX_FLOOR = 10

    current_floor = int(input("Enter current floor: "))

    requests = input_handler()

    processed_requests = manage_requests(requests, MIN_FLOOR, MAX_FLOOR)

    total_time = 0
    movement_log = []

    for floor in processed_requests:
        path = move_elevator(current_floor, floor)
        movement_log.extend(path)

        total_time += calculate_time(current_floor, floor)
        current_floor = floor

    print("\nElevator Movement:")
    for floor in movement_log:
        print(f"Reached floor {floor}")

    print(f"\nTotal time taken: {total_time} units")


if __name__ == "__main__":
    elevator_controller()
