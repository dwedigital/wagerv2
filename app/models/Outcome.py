""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to


class Outcome(Model):
    """Outcome Model"""

    @belongs_to('wager_id', 'id')
    def wager(self):
        from app.models.Wager import Wager
        return Wager
