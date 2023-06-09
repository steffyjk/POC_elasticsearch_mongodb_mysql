import os
from dotenv import load_dotenv

load_dotenv()


class Elastic:
    """Class which stores the elasticsearch credentials"""
    hosts = [os.environ['ES_HOSTS']]
    user = None
    password = None

    def __init__(self):
        self.user = os.environ.get("ES_USER")
        self.password = os.environ.get("ES_PASSWORD")


Credentials = Elastic()

