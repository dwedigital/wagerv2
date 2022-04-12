from masonite.authentication import Auth
from masonite.request import Request
from app.models.User import User


class WagerAnalytics:
    def __init__(self, wagers, user):
        self.wagers = wagers
        self.user = user
        self.won = 0
        self.lost = 0
        self.win_percentage = None
        self.winnings = 0
        self.losings = 0
        self.user_id = User.where("email", self.user.email).first().id
        # Get the wins and losses

        for i in self.wagers:
            try:
                if i.outcome.winner_id == self.user_id:
                    self.won += 1
            except:
                pass
            try:
                if i.outcome.loser_id == self.user_id:
                    self.lost += 1
            except:
                pass

        # Get the win percentage
        if self.won + self.lost > 0:
            self.win_percentage = round((self.won / (self.won + self.lost)) * 100, 2)

    def status(self):
        wagers_by_status = {}
        for wager in self.wagers:
            if wager.referee != self.user.email:
                if wager.status in wagers_by_status:
                    wagers_by_status[wager.status] += 1
                else:
                    wagers_by_status[wager.status] = 1
        return wagers_by_status

    def total(self):
        return len(self.wagers)

    def amount_won(self):
        for i in self.wagers:
            if i.outcome and i.reward:
                if (
                    i.outcome.winner_id == self.user_id
                    and i.status == "complete"
                    and i.reward.amount
                ):
                    self.winnings += i.reward.amount

        return self.winnings

    def amount_lost(self):
        for i in self.wagers:
            if i.outcome and i.reward:
                if (
                    i.outcome.loser_id == self.user_id
                    and i.status == "complete"
                    and i.reward.amount
                ):
                    self.losings += i.reward.amount

        return self.losings

    def reward_types(self):
        reward_types = {}
        for i in self.wagers:
            if i.reward:
                if i.reward.reward_type in reward_types:
                    reward_types[i.reward.reward_type] += 1
                else:
                    reward_types[i.reward.reward_type] = 1
        return reward_types
