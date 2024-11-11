from os import getenv


def dep_env():
    return {
        "SPARKPOST": {
            "API_KEY": getenv("SPARKPOST_API_KEY", ""),
            "IS_SANDBOX": getenv("SPARKPOST_IS_SANDBOX", True),
            "FROM_EMAIL": getenv("SPARKPOST_FROM_EMAIL", "")
        },
        "TWILIO": {
            "API_KEY": getenv("TWILIO_API_KEY", ""),
            "FROM_EMAIL": getenv("TWILIO_FROM_EMAIL", "")
        }
    }
