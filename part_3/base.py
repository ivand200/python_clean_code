"""Design by contract"""
# That is to say that if, for example, we have a function that is expected to work with
# a series of parameters of type integers, and some other function invokes ours by
# passing strings, it is clear that it should not work as expected, but in reality, the
# function should not run at all because it was called incorrectly (the client made a
# mistake). This error should not pass silently.


import logging 


config = {"dbport": 5432}
print(config.get("dbport", "localhost"))

def connect_database(host="localhost", port=5432):
    """Default args"""
    logging.info("connecting to database server at %s:%i", host, port)


class Connector:
    """Abstract the connection to a database"""

    def connect(self):
        """Connect to a data source"""
        return self

    @staticmethod
    def send(data):
        return data


class Event:
    def __init__(self, payload):
        self._payload = payload

    def decode(self):
        return f"decoded {self._payload}"
