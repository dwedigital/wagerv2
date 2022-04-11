from masonite.mail import Mailable


class NewChallenge(Mailable):
    def build(self):
        return (
            self.subject("You've Been Challenged to a Wager")
            .from_("admin@gmail.com")
            .text("Hello from Masonite!")
            .html("<h1>Hello from Masonite!</h1>")
        )
