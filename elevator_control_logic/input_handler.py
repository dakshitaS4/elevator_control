def input_handler():
    floors = input("Enter floor requests separated by space: ")
    requests = list(map(int, floors.split()))
    return requests
