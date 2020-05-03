from flask import Flask


import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://41f363dac0a54744bfb4e6cbfc40de8e@o304275.ingest.sentry.io/5221872",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0


@app.route('/')
@app.route('/hello')
def hello():
    return 'hi'