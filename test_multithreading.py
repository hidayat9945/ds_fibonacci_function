#multitrhreading
# %%time -- uncomment for jupyter or collabs

import threading
import time
from find_fibo import find_fibonacci

threads = []

start = time.perf_counter()
for num in range(100):
  t = threading.Thread(target=find_fibonacci, args=[num])
  t.start()
  threads.append(t)

for thread in threads:
  thread.join()

finish = time.perf_counter()

executed_time = round(finish - start, 2)
print(f"Finished in {executed_time} second(s)")
