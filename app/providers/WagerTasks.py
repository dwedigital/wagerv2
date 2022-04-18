from masonite.providers import Provider
from app.tasks.ExpiredWagers import ExpiredWagers


class WagerTasks(Provider):
    def __init__(self, application):
        self.application = application

    def register(self):
        self.application.make('scheduler').add(
            ExpiredWagers().daily_at(8)
        )

    def boot(self):
        pass
