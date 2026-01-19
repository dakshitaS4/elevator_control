from validator import validate_request


def is_duplicate(floor, request_list):
    """
    Checks whether a floor is already present in the request list
    """
    if floor in request_list:
        return True
    return False


def manage_requests(requests, min_floor, max_floor):
    """
    Filters, removes duplicates, and sorts elevator floor requests
    """
    valid_requests = []

    for floor in requests:
        if validate_request(floor, min_floor, max_floor):

            if not is_duplicate(floor, valid_requests):
                valid_requests.append(floor)

    valid_requests.sort()

    return valid_requests
