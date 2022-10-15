"""The open/close principle"""


from databases import dataclass


@dataclass
class Event:
    raw_data: dict

    @staticmethod
    def meets_condition(event_data: dict):
        return False


class UnknownEvent(Event):
    """A type of event that cannot be identified fro its data"""


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0
        )


class TransactionEvent(Event):
    """Represents a transaction that just occurred on the system."""

    @staticmethod
    def meets_condition(event_data: dict):
        return event_data["after"].get("transaction") is not None


class SystemMonitor:
    """Identify events that occureed in the system

    >>> l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    >>> l1.identify_event().__class__.__name__
    'LoginEvent'

    >>> l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    >>> l2.identify_event().__class__.__name__
    'LogoutEvent'

    >>> l3 = SystemMonitor({"before": {"session": 1}, {"after": {"session": 1}}})
    >>> l3.identify_event().__class__.__name__
    'TransactionEvent'
    """

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnknownEvent(self.event_data)