# python-rq-sklearn minimal app

Minimal app using redis queues. Similar to the example in the rq site [here](https://python-rq.org/docs/), but using with a machine learning model as the job.

This app predicts the iris species using a random forest classifier model trained on the [iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set). The four input features are the sepal length, the sepal width, the petal length and the petal width.

The app uses redis queues to send the prediction jobs to a worker process. After submiting the job, it prints the result immediately, which should result in `None` as output. Then it waits five seconds and prints the result after the worker has finished the job.

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

In a new terminal activate the environment and then start the worker. This also trains the model that will be used in all predictions.

```bash
source .venv/bin/activate
python worker.py
```

In yet another terminal, activate the environment and then start the app to submit the jobs

```bash
source .venv/bin/activate
python -u app.py
```

Pass four extra arguments to use as input in the model. Otherwise input values from the dataset are used. For example:

```bash
(.venv)$ python app.py .1 .2 .3 .4
Predicting on:
[[0.1, 0.2, 0.3, 0.4]]
Immediately:
None
After waiting for 3 seconds:
setosa
```
