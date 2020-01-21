from rq import Queue
from redis import Redis
from countwords import count_words_at_url
import time
import sys

# settings
wait_seconds = 5
default_site = 'http://nvie.com'

# Tell RQ what Redis connection to use
redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue

# set the sites to count words on
if len(sys.argv) > 1:
    sites = sys.argv[1:]
else:
    sites = [default_site]

print(f'Checking the number of words on {", ".join(sites)}')
print("Immediately:")
jobs = [q.enqueue(count_words_at_url, site) for site in sites]
# check the result before they are complete
for job in jobs:
    print(job.result)   # => None

# Now, wait a while, until the worker is finished and check again
print(f"After waiting for {wait_seconds} seconds:")
time.sleep(wait_seconds)
for job in jobs:
    print(job.result)   # => 337 or something 
