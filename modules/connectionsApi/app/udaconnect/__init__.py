from .models import Connection, Person
from .schemas import ConnectionSchema, PersonSchema


def register_routes(api, app, root="personsApi"):
    from .controllers import api as udaconnect_api

    api.add_namespace(udaconnect_api, path=f"/{root}")
