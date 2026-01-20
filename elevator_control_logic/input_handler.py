def input_handler():
    floors = input("Enter floor requests separated by space: ")
    return list(map(int, floors.split()))
