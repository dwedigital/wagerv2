"""Task Module Description"""
from masonite.scheduling import Task
from masonite.facades import Mail
from app.mailables.WagerExpired import WagerExpired
from app.mailables.WagerExpiredRef import WagerExpiredRef

from app.models.Wager import Wager


class ExpiredWagers(Task):
    def handle(self):
        wagers = Wager.all()
        for wager in wagers:
            if wager.expired():
                print(f"Wager {wager.id} has expired")
                Mail.mailable(WagerExpired(wager).to(wager.proposer)).send()
                Mail.mailable(WagerExpired(wager).to(wager.challenger)).send()
                
                if wager.referee:
                    Mail.mailable(WagerExpiredRef(wager).to(wager.referee)).send()
                
                
                
