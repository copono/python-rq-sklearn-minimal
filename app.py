from rq import Queue
from redis import Redis
import time, sys
from model import get_data, predict, to_target_names
import numpy as np
# settings
wait_seconds = 3

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue

# Take the input from the user or the test dataset.
if len(sys.argv)==5:
    X_predict = [[float(i) for i in sys.argv[1:]]]
else:
    _, X_test, _, y_test = get_data()
    X_predict = X_test[:3]

# submit the job
job = q.enqueue(predict, X_predict)

print('Predicting on:')
print(X_predict)
print('Checking the job immediately we get:')
# check the result before they are complete
print(to_target_names(job.result))   # => None

# Now, wait a while, until the worker is finished and check again
print(f"After waiting for {wait_seconds} seconds we get:")
time.sleep(wait_seconds)
print(to_target_names(job.result))    # => [0, 1, 2] or something
