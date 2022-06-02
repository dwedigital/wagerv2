from masonite.queues import Queueable
from app.mailables.NewChallenge import NewChallenge
from masonite.facades import Mail


class SendNewChallengeEmail(Queueable):
    def __init__(self, wager) -> None:
        self.wager = wager
    def handle(self):
        print("CHALLENGER: ", self.wager.challenger)
        Mail.mailable(NewChallenge(self.wager).to(self.wager.challenger)).send()
