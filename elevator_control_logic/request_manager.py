# from validator import validate_request


# def is_duplicate(floor, request_list):
#     """
#     Checks whether a floor is already present in the request list
#     """
#     if floor in request_list:
#         return True
#     return False


# def manage_requests(requests, min_floor, max_floor):
#     """
#     Filters, removes duplicates, and sorts elevator floor requests
#     """
#     valid_requests = []

#     for floor in requests:
#         if validate_request(floor, min_floor, max_floor):

#             if not is_duplicate(floor, valid_requests):
#                 valid_requests.append(floor)

#     valid_requests.sort()

#     return valid_requests




from validator import validate_request

class RequestManager:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor

    def process_requests(self, requests):
        valid_requests = []

        for floor in requests:
            if validate_request(floor, self.min_floor, self.max_floor):
                if floor not in valid_requests:
                    valid_requests.append(floor)

        valid_requests.sort()
        return valid_requests
