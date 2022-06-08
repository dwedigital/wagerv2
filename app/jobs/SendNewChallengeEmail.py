from masonite.queues import Queueable
from app.mailables.NewChallenge import NewChallenge
from masonite.facades import Mail
from app.models.Message import Message


class SendNewChallengeEmail(Queueable):
    def __init__(self, wager) -> None:
        self.wager = wager
    def handle(self):
        print("CHALLENGER: ", self.wager.challenger)
        Message.create({"message_status_id":1,
        "wager_id":self.wager.id})
        Mail.mailable(NewChallenge(self.wager).to(self.wager.challenger)).send()
