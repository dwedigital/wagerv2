""" User Model """
import uuid
from masoniteorm.models import Model
from masoniteorm.relationships import has_one


class Wager(Model):
    """Wager Model"""
    __fillable__ = ["name", "description", "challenger", "proposer", "referee", "expiry_date", "status"]
    __dates__ = ['expiry_date']

    def __init__(self):
        super().__init__()
        self.token = str(uuid.uuid4())

    @has_one('id','id')
    def reward(self):
        from app.models.Reward import Reward
        return Reward

    @has_one('id','id')
    def outcome(self):
        from app.models.Outcome import Outcome
        return Outcome



    def get_challenger(self):
        from app.models.User import User
        user = User.where('email', self.challenger).first()
        if(user):
            return user
        else:
            return None
    

    def get_proposer(self):
        from app.models.User import User
        user= User.where('email', self.proposer).first()
        if(user):
            return user
        else:
            return None



    def get_referee(self):
        from app.models.User import User
        user =  User.where('email', self.referee).first()
        if(user):
            return user
        else:
            return None


        
