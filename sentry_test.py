import sentry_sdk
sentry_sdk.init("https://41f363dac0a54744bfb4e6cbfc40de8e@o304275.ingest.sentry.io/5221872")


division_by_zero = 1 / 0


sentry_sdk.capture_exception(Exception("This is an example of an error message."))
