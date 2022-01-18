import datetime as dt

# STOPWATCH CLASS
# Start, stop, reset, lap methods. Expanded functionality for iterative functions.
class Stopwatch:
    __last_lap_time = None
    __start_time = None
    __end_time = None
    total_duration = 0.0
    average_lap_time = 0.0
    lap_times = []
    
    def __init__(self):
        self.lap_times = []
        self.__last_lap_time = None
        self.__start_time = None
        self.__end_time = None
        self.total_duration = 0.0
        self.average_lap_time = 0.0
    
    def __generate_stats(self):
        self.total_duration = self.lap_times.sum()
        self.average_lap_time = self.total_duration / len(self.lap_times)

    def start(self, log_output = False):
        self.__start_time = dt.datetime.now()
        self.__last_lap_time = self.__start_time

        if log_output:
            print("Stopwatch started!")
    
    def lap(self, log_output = False):
        curr_time = dt.datetime.now()
        duration = (curr_time - self.__last_lap_time).seconds # Capture the duration
        self.lap_times.append(duration) # Append duration to list
        self.__last_lap_time = curr_time # Update lap time

        if log_output:
            print(f"Lap: {duration} seconds")

    def end(self, log_output = False):
        self.__end_time = dt.datetime.now()
        duration = self.__end_time - self.__last_lap_time
        self.lap_times.append(duration)
        self.__generate_stats() # Create statistics

        if log_output:
            print(f"""Stopwatch Stopped!
            Total duration: {self.total_duration}
            No. laps: {len(self.lap_times)}
            Average lap time: {self.average_lap_time}
            Longest lap: {self.lap_times.max()}
            Shortest lap: {self.lap_times.min()}
            """)

    def reset(self, log_output = False):
        self.__last_lap_time = None
        self.__start_time = None
        self.__end_time = None
        self.total_duration = 0.0
        self.average_lap_time = 0.0
        self.lap_times = []

        if log_output:
            print("Stopwatch reset!")