from os import getenv


def dep_env():
    return {
        "SPARKPOST": {
            "API_KEY": getenv("SPARKPOST_API_KEY", ""),
            "IS_SANDBOX": getenv("SPARKPOST_IS_SANDBOX", "true") in ["1", "True", "true"],
            "FROM_EMAIL": getenv("SPARKPOST_FROM_EMAIL", "")
        },
        "MAILJET": {
            "API_KEY": getenv("MAILJET_API_KEY", ""),
            "SECRET_KEY": getenv("MAILJET_SECRET_KEY", ""),
            "FROM_EMAIL": getenv("MAILJET_FROM_EMAIL", ""),
            "FROM_NAME": getenv("MAILJET_FROM_NAME", "")
        }
    }
