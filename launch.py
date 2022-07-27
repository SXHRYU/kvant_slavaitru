import subprocess


subprocess.run(
    [
    "python ./manage.py create_executors",
    "python ./manage.py random_ops",
    "python ./manage.py choose"
    ], capture_output=True)
