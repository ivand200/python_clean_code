from typing import Iterable, Set
import re


def run_calculation(i):
    return i + 1


numbers = [run_calculation(i) for i in range(10)]


def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    """
    Given several ARNs in the form
    arn:partition:service:region:account-id:resource-id
    Collect the unique account IDs found on those strings, and return them
    """
    matched_arns = filter(None, (re.match(ARN_REGEX, arn) for arn in arns))
    return {m.groupdict()["account_id"] for m in matched_arns}


def collect_account_ids_from_arns(arns: Iterable[str]) -> Set[str]:
    return {
        matched.groupdict()["account_id"]
        for arn in arns
        if (matched:= re.match(ARN_REGEX, arn)) is not None
    }

#  Page 43