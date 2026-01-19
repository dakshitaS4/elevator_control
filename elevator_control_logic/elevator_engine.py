def move_elevator(current_floor, target_floor):
    path = []

    while current_floor < target_floor:
        current_floor += 1
        path.append(current_floor)

    return path
