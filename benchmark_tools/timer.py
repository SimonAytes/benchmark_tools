import datetime as dt

# TIMER CLASS
# Start, stop, reset methods. Basic use cases for timing individual functions.
class Timer:
    __start_time = None
    __end_time = None
    duration = 0.0
    
    def __init__(self):
        self.__start_time = None
        self.__end_time = None
    
    def __update_end_time(self):
        self.duration = self.__end_time = self.__start_time

    def start(self, log_output = False):
        self.__start_time = dt.datetime.now()
        
        if log_output:
            print("Timer started!")

    def stop(self, log_output = False):
        self.__end_time = dt.datetime.now()
        self.__update_end_time()

        if log_output:
            print(f"Timer stopped! Duration: {self.duration}")

    def reset(self, log_output = False):
        self.__start_time = None
        self.__end_time = None

        if log_output:
            print("Timer reset!")
