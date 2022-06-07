""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class Message(Model):
    """Message Model"""
    __fillable__ = [
        "message_status_id",
        "wager_id"
    ]

    @has_one("id", "wager_id")
    def wager(self):
        from app.models.Wager import Wager
        return Wager
    
    @has_one("id", "message_status_id")
    def messageStatus(self):
        from app.models.MessageStatus import MessageStatus
        return MessageStatus
