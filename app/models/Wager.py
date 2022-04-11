""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class Wager(Model):
    """Wager Model"""
    __fillable__ = ["name", "description", "challenger_id", "proposer_id", "referee_id"]

    @has_one('id','id')
    def reward(self):
        from app.models.Reward import Reward
        return Reward

    @has_one('id','id')
    def outcome(self):
        from app.models.Outcome import Outcome
        return Outcome

    has_one('id','id')
    def challenger(self):
        from app.models.User import User
        return User
    
    has_one('id','id')
    def proposer(self):
        from app.models.User import User
        return User

    has_one('id','id')
    def referee(self):
        from app.models.User import User
        return User

    