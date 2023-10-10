import functions

import time
start_time = time.time()

print(functions.longestCollatz(1000000))

print("--- %s seconds ---" % (time.time() - start_time))

