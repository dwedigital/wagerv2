from masonite.authentication import Auth
from masonite.request import Request
from app.models.User import User

class WagerAnalytics():
    def __init__(self, wagers, user):
        self.wagers = wagers
        self.user = user
        self.won = 0
        self.lost = 0
        self.win_percentage = None

        # Get the wins and losses
        user_id = User.where('email',self.user.email).first().id
        for i in self.wagers:
            try:
                if i.outcome.winner_id == user_id:
                    self.won += 1
            except:
                pass
            try:
                if i.outcome.loser_id == user_id:
                    self.lost += 1
            except:
                pass

        # Get the win percentage
        if self.won + self.lost > 0:
            self.win_percentage = round((self.won / (self.won + self.lost)) * 100, 2)

    def status(self):
        wagers_by_status = {}
        for wager in self.wagers:
            if wager.status in wagers_by_status:
                wagers_by_status[wager.status] += 1
            else:
                wagers_by_status[wager.status] = 1
        return wagers_by_status



    def total(self):
        return len(self.wagers)