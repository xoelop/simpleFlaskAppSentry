# Simple project to try out sentry, it doesn't work
I'm trying to use Sentry to track errors on one of my projects and can't get it to work. It should be the simplest thing and I used it some months ago in another project, so I don't know what I'm doing wrong. 

This is a simple project to make it work but it's still not working

## Installation
Run `pipenv install`

## Running

When doing `python sentry_test.py`, two errors should be sent to sentry. Doesn't happen and this is the output in the terminal:
```
Traceback (most recent call last):
  File "test.py", line 5, in <module>
    division_by_zero = 1 / 0
ZeroDivisionError: division by zero
Sentry is attempting to send 0 pending error messages
Waiting up to 2 seconds
Press Ctrl-C to quit
```

The most strange line is that `Sentry is attempting to send 0 pending error messages`. Why 0 instead of 2?

Also, when running the flask app locally with `flask run` and going to http://localhost:5000/debug-sentry, no errors are sent to Sentry