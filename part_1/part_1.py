"""Part 1"""

from typing import Tuple, List, Union
import logging


d = {}
d.update({1: "one", 2: "two"})
d.update([(3, "three"), (4, "four")])
# d.update(five=5)
print(d)


Seconds = float
def launch_task(delay: Seconds):
    """
    Docstring
    """
    return delay + 5

print(launch_task(4))


# it's better to be explicit and have
# a name for that alias, so we don't have to infer what that type means:
Client = Tuple[int, str]
def process_clients(clients: List[Client]):
    """
    Docstring
    """
    return clients[1]


# mypy <filename>
# pylint part_1/part_1.py
# black -l 79 *.py
# black -- check part_1/part_1.py
# make checklist
def broadcast_notification(
    message: str,
    relevant_user_emails: Union[List[str], Tuple[str]]
):
    """
    Docstring
    """
    for email in relevant_user_emails:
        logging.info("Sending %r to %r", message, email)
