import datetime as dt

# STOPWATCH CLASS
# Start, stop, reset, lap methods. Expanded functionality for iterative functions.
class Stopwatch:
    __start_time = None
    __end_time = None
    __last_lap_time = None
    __total_duration = None
    __average_lap_time = None
    __lap_times = []
    __sys_log = False
    
    def __init__(self, logActions = False):
        self.lap_times = []
        self.__start_time = None
        self.__end_time = None
        self.__last_lap_time = None
        self.__total_duration = 0.0
        self.__average_lap_time = 0.0
        self.__sys_log = logActions
    
    def __generate_stats(self):
        self.__total_duration = sum(self.__lap_times)
        self.__average_lap_time = self.__total_duration / len(self.__lap_times)

    # Start the timer
    def start(self):
        self.reset()
        self.__start_time = dt.datetime.now()
        self.__last_lap_time = self.__start_time

        if self.__sys_log:
            print("Stopwatch started!")
    
    # Lap the timer
    def lap(self):
        curr_time = dt.datetime.now()
        duration = (curr_time - self.__last_lap_time).seconds # Capture the duration
        self.__lap_times.append(duration) # Append duration to list

        if self.__sys_log:
            print(f"Lap: {duration} seconds")

    # Stop the timer
    def stop(self):
        self.__end_time = dt.datetime.now()
        duration = self.__end_time - self.__last_lap_time
        self.lap_times.append(duration)
        self.__generate_stats() # Create statistics

    # Print summary
    def summary(self):
        print(f"""Stopwatch Stopped!
            Total duration:     {self.__total_duration} seconds
            No. iterations:     {len(self.__lap_times)}

            Average lap time:   {self.__average_lap_time} seconds
            Longest lap:        {max(self.lap_times)} seconds
            Shortest lap:       {min(self.lap_times)} seconds

            Started at:         {self.__start_time}
            Ended at:           {self.__end_time}
            """)

    def reset(self, log_output = False):
        self.__last_lap_time = None
        self.__start_time = None
        self.__end_time = None
        self.total_duration = 0.0
        self.average_lap_time = 0.0
        self.lap_times = []

        if self.__sys_log:
            print("Stopwatch reset!")