from masonite.configuration import config
from masonite.mail import Mailable

from app.models.Wager import Wager


class NewChallenge(Mailable):
    def __init__(self, wager: Wager):
        super().__init__()
        self.wager = wager

    def build(self):
        print("email sent")
        return (
            self.subject("You've Been Challenged to a Wager")
            .from_(config("mail.from_address"))
            .view("wager.mailables.newwagerchallenger", {"wager": self.wager})
        )
