from masonite.configuration import config
from masonite.mail import Mailable

from app.models.Wager import Wager


class WagerExpiredRef(Mailable):
    def __init__(self, wager: Wager):
        super().__init__()
        self.wager = wager

    def build(self):
        return (
            self.subject(f"{self.wager.name} has expired")
            .from_(config("mail.from_address"))
            .view("wager.mailables.expiredwagerref", {"wager": self.wager})
        )
