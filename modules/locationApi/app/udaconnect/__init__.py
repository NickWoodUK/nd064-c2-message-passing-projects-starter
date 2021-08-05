from modules.locationApi.app.udaconnect.models import Location
from modules.locationApi.app.udaconnect.schemas import LocationSchema


def register_routes(api, app, root="api"):
    from modules.locationApi.app.udaconnect.controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
