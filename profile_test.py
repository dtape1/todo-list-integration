import cProfile
import pstats
import io
from task_manager import TaskManager

def benchmark():
    m = TaskManager()
    for i in range(1000):
        m.add_task(f"Task {i}")
    for i in range(500):
        m.edit_task(i, f"New {i}")
    for i in range(199, -1, -1):
        m.delete_task(i)

pr = cProfile.Profile()
pr.enable()
benchmark()
pr.disable()

s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats("cumulative")
ps.print_stats(10)
print(s.getvalue())