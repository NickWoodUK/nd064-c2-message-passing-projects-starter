from generated import location_pb2_grpc
#from .generated import location_pb2_grpc

#from generated import location_pb2

#from app import db

#from models import Location


class locationServicer(location_pb2_grpc.LocationsServicer):
    def Get(self, request, context):

        comm= '''
            metadata = dict(context.invocation_metadata())
            print(metadata)
    
            location_id = request.id
    
            location, coord_text = (
                db.session.query(Location, Location.coordinate.ST_AsText())
                    .filter(Location.id == location_id)
                    .one()
            )
    
            # Rely on database to return text form of point to reduce overhead of conversion in app code
            location.wkt_shape = coord_text
            return location
        '''

        location = Location
        location.id = 10

        return location