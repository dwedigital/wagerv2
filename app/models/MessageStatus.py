""" User Model """

from masoniteorm.models import Model


class MessageStatus(Model):
    """MessageStatus Model"""
    __fillable__ = ["id","status"]

    pass
