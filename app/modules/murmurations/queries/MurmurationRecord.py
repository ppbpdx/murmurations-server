from graphene import ObjectType, Field, List
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from app.models.Model import Record as RecordModel


class RecordType(SQLAlchemyObjectType):
    class Meta:
        model = RecordModel
        exclude_fields = ("origin",)


class MurmurationRecord(ObjectType):
    murmuration = Field(
        List(RecordType),
        description=
        """
        :description: Returns the Murmuration Object.
        """
    )

    def resolve_murmuration(self, info):
        record = RecordModel.query.all()
        if record:
            return record
        else:
            raise GraphQLError("No record  found.")
