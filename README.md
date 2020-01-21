# python-rq minimal app

Minimal app using redis pub/sub. Based on the rq site example [here](https://python-rq.org/docs/).

This app sends a redis queue job to the worker, which counts the words in a website. The app prints the result of the jobs immediately after the job submissions, which should result in `none` as output. Then it waits five seconds and prints the result after the worker has finished the job.

## Setup

This project requires redis and python with the rq and requests libraries.

On mac install redis with `brew install redis`

Then set the environment for python with

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

First run the redis server using

```bash
redis-server redis.conf
```

In a new terminal activate the environment and then start the worker with

```bash
source .venv/bin/activate
rq worker
```

In yet another terminal, activate the environment and then start the app that submits the jobs using

```bash
source .venv/bin/activate
python -u app.py
```

Pass extra arguments to check the number of words in those sites. Otherwise default websites are used. For example:

```bash
(.venv)$ python -u app.py http://wikipedia.org https://stackoverflow.com
Checking the number of words on http://wikipedia.org, https://stackoverflow.com
Immediately:
None
None
After waiting for 5 seconds:
3547
7437
```
