"""Handling exception"""
# Handling the exception itself can mean multiple things. In its simplest form, it could
# be just about logging the exception (make sure to use logger.exception or logger.
# error to provide the full context of what happened).


import logging
import time

from part_3.base import Connector, Event

logger = logging.getLogger(__name__)

def connect_with_retry(
    connector: Connector, retry_n_times: int, retry_backoff: int = 5
):
    """
    Tries to establish the connection of <connector> retrying
    <retry_n_times>, and waiting <retry_baackoff> seconds between attemps.

    if it can connect, returns the connection object.
    if it's not possible to connect after the retries have been exhausted,
    raises ''ConnectionError''.

    :param connector: An object with a ''.connect()'' method.
    :param retry_n_times int: The number of times to try to call ''connector.connect()''.
    :param retry_backoff int: The time lapse between retry calls.
    """
    for _ in range(retry_n_times):
        try:
            return connector.connect()
        except ConnectionError as e:
            logger.info(
                "%s: attempting new connection in %s", e, retry_backoff
            )
            time.sleep(retry_backoff)
        exc = ConnectionError(f"Couldn't connect after {retry_n_times} times")
        logger.exception(exc)
        raise exc


class DataTransport:
    """
    An example of object that separates the exception handling by
    abstraction levels
    """
    _RETRY_BACKOFF: int = 5
    _RETRY_TIMES: int = 3

    def connect_with_retry():
        pass

    def __init__(self, connector: Connector) -> None:
        self._connector = connector
        self.connection = None

    def deliver_event(self, event: Event):
        self.connection = connect_with_retry(
            self._connector,
            self._RETRY_TIMES,
            self._RETRY_BACKOFF
        )
        self.send(event)

    def send(self, event: Event):
        try:
            return self.connection.send(event.decode())
        except ValueError as e:
            logger.error("%r contains incorrect data: %s", event, e)
            raise
