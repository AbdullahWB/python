import numpy as np
import time

size = 1_000_000_000
l1 = np.array(list(range(size)))
l2 = np.array(list(range(size)))
start = time.time()
add = l1 + l2
end = time.time()
print(end - start)