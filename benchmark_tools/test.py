from multiprocessing.resource_sharer import stop
import stopwatch as sw
import time
import random

sw = sw.Stopwatch()

sw.start()

for i in range(0, 100):
    time.sleep(random.uniform(0.02, 0.8))
    sw.lap()

sw.stop()

sw.summary()