# python-rq-hello

Hello world app using redis pub/sub. Based on the rq site example [here](https://python-rq.org/docs/)

The app sends a redis queue job to the worker, which counts the words in a website. Then the app prints that number.

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

First run the redis server with `redis-server redis.conf`.

In a new terminal activate the environment and then start the worker with `rq worker`.

In yet another terminal, activate the environment, and start the app that will submit the job using `python -u app.py`.
