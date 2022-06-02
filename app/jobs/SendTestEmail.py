from masonite.queues import Queueable
from masonite.facades import Mail
from app.mailables.Test import Test


class SendTestEmail(Queueable):
    def __init__(self, person: str) -> None:
        self.person = person
    def handle(self):
        res =  Mail.mailable(Test().to(self.person)).send()
        print(res.status_code)
