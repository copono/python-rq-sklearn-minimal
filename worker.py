import sys
from rq import Connection, Worker
from model import train, get_data

# Provide queue names to listen to as arguments to this script,
# similar to rq worker
with Connection():
    qs = sys.argv[1:] or ['default']
    train()
    w = Worker(qs)
    w.work()