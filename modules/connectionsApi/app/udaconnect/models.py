from __future__ import annotations

from dataclasses import dataclass

from app import db  # noqa


@dataclass
class Connection:
    location: Location
