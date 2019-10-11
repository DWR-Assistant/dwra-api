from datetime import datetime
from peewee import CharField, IntegerField, DateTimeField

from models.base import BaseModel

class Account(BaseModel):
    id = IntegerField(primary_key=True, null=False)
    nickname = CharField(null=False)
    avatar = CharField(null=False)
    username = CharField()
    password = CharField()
#    authentications = EmbeddedDocumentField(Authentications)
    created_time = DateTimeField(default=datetime.utcnow())
    updated_time = DateTimeField()

    @classmethod
    def get_by_wxapp(cls, openid):
        null
