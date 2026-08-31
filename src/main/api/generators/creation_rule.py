from dataclasses import dataclass


@dataclass
class CreationRule:
    regex: str
    min_value: float | None = None
    max_value: float | None = None