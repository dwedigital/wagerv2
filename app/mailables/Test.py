from masonite.mail import Mailable


class Test(Mailable):
    def build(self):
        return (
            self.subject("Masonite 4")
            .from_("admin@gmail.com")
            .text("Hello from Masonite!")
            .html("<h1>Hello from Masonite!</h1>")
        )
