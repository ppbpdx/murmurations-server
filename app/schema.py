from graphene import ObjectType, Schema, String

from app.modules.murmurations.mutations import UpdateMutation, UpdateRecords

from graphene import ObjectType

from app.modules.murmurations.queries.MurmurationRecord import MurmurationRecord


class RecordQuery(MurmurationRecord, ObjectType):
    pass


class RootQuery(RecordQuery, ObjectType):
    pass



class RootMutation( ObjectType):
    update_cache = UpdateRecords.Field()


schema = Schema(query=RootQuery, mutation=RootMutation)
