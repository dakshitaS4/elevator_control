def validate_request(floor, min_floor, max_floor):
    if floor < min_floor or floor > max_floor:
        return False
    return True
