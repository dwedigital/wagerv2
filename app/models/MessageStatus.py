""" User Model """

from masoniteorm.models import Model


class MessageStatus(Model):
    """MessageStatus Model"""
    __timestamps__ = None
    __fillable__ = ["id","message"]

    pass
