#import benchmark_tools as bt
import benchmark_tools


sw = benchmark_tools.Stopwatch()

sw.start()

for i in range(0, 100):
    temp = i * 100000 / 4 + 411
    sw.lap()

sw.stop(True)