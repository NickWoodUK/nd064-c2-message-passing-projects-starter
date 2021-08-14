from __future__ import annotations

from dataclasses import dataclass

from app import db  # noqa
from sqlalchemy import Column, Integer, String

from modules.locationApi.app.udaconnect.models import Location


class Person(db.Model):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)