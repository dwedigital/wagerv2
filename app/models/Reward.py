""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class Reward(Model):
    """Reward Model"""

    __fillable__ = ["wager_id", "description", "amount", "reward_type"]

    @belongs_to("wager_id", "id")
    def wager(self):
        from app.models.Wager import Wager

        return Wager
