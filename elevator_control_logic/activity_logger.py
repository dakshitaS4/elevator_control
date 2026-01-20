# class Logger:
#     def __init__(self, filename="elevator_log.txt"):
#         self.filename = filename

#     def log(self, message):
#         with open(self.filename, "a") as file:
#             file.write(message + "\n")




from abc import ABC, abstractmethod

class BaseLogger(ABC):
    @abstractmethod
    def log(self, message):
        pass


class FileLogger(BaseLogger):
    def __init__(self, filename="elevator_log.txt"):
        self.filename = filename

    def log(self, message):
        with open(self.filename, "a") as file:
            file.write(message + "\n")


class ConsoleLogger(BaseLogger):
    def log(self, message):
        print("[LOG]", message)
