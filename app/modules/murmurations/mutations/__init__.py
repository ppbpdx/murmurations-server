from graphene import AbstractType, String

from .UpdateMurmurations import UpdateRecords


class UpdateMutation(AbstractType):
    record_type = String()
