"""Dataclass"""


from typing import List
from databases import dataclass, field

R = 26

@dataclass
class RTrieNode:
    size = R
    values: int
    next_: List["RTrieNode"] = field(
        default_factory=lambda: [None] * R
    )

    def __post_init__(self):
        if len(self.next_) != self.size:
            raise ValueError(f"Invalid length provided for next list")