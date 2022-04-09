""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many


class Wager(Model):
    """Wager Model"""
    __fillable__ = ["name", "description", "challenger_id", "proposer_id", "referee_id"]
