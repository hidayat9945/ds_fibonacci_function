#async
import time
from find_fibo import find_fibonacci 

# %%time

start = time.perf_counter()
for i in range(1,101):
  # print(f'fibo number {i} is')
  print(find_fibonacci(i))
finish = time.perf_counter()

executed_time = round(finish - start, 2)
print(f"Finished in {executed_time} second(s)")
