"""A WelcomeController Module."""
from masonite.controllers import Controller
from masonite.views import View


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("welcome")
