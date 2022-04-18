"""Task Module Description"""
from masonite.scheduling import Task

from app.models.Wager import Wager


class ExpiredWagers(Task):
    def handle(self):
        wagers = Wager.all()
        for wager in wagers:
            if wager.expired():
                print(f"Wager {wager.id} has expired")
                # TODO add mailable to send email to proposer and challenger if no referee
                # TODO add mailable to send email to referee if referee
                
