from collections.abc import Mapping


class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False

    @staticmethod
    def validate_precondition(event_data: dict):
        """
        Precondition of the contract of this interface.
        Validate that the 'event_data' parameter is properly formed.
        """
        if not isinstance(event_data, Mapping):
            raise ValueError(f"{event_data!r} is not a dict")
        for moment in ("before", "after"):
            if moment not in event_data:
                raise ValueError(f"{moment} not in {event_data}")
            if not isinstance(event_data[moment], Mapping):
                raise ValueError(f"event_data[{moment!r}] is not a dict")


class UnknownEvent(Event):
    """
    A type of event that cannot be identified from its data
    """


# class LoginEvent(Event):
#     @staticmethod
#     def meets_condition(event_data: dict) -> bool:
#         return super().meets_condition(event_data)


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"].get("session") == 0
            and event_data["after"].get("session") == 1
        )


class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"].get("session") == 1
            and event_data["after"].get("session") == 0
        )


class TransactionEvent(Event):
    """
    Represents a transaction that has just occurred on the system.
    """

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
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