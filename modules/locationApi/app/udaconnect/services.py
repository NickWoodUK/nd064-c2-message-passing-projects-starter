import logging
from typing import Dict

import geoalchemy2.functions

from modules.personsApi.app import db
from modules.locationApi.app.udaconnect.models import Location
from modules.locationApi.app.udaconnect.schemas import LocationSchema

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-personsApi")


class LocationService:
    @staticmethod
    def retrieve(location_id) -> Location:
        location, coord_text = (
            db.session.query(Location, Location.coordinate.ST_AsText())
                .filter(Location.id == location_id)
                .one()
        )

        # Rely on database to return text form of point to reduce overhead of conversion in app code
        location.wkt_shape = coord_text
        return location

    @staticmethod
    def create(location: Dict) -> Location:
        validation_results: Dict = LocationSchema().validate(location)
        if validation_results:
            logger.warning(f"Unexpected data format in payload: {validation_results}")
            raise Exception(f"Invalid payload: {validation_results}")

        new_location = Location()
        new_location.person_id = location["person_id"]
        new_location.creation_time = location["creation_time"]
        new_location.coordinate = ST_Point(location["latitude"], location["longitude"])
        db.session.add(new_location)
        db.session.commit()

        return new_location
