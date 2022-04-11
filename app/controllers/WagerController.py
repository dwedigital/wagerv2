from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from app.models.Wager import Wager
from app.models.Reward import Reward


class WagerController(Controller):
    def index(self, view: View, request: Request, response: Response):
        return view.render("wager.home")

    def wager(self, view: View, request: Request, response: Response):
        # TODO add wager wager
        wager = Wager.find(request.param("id"))
        if wager:
            return view.render("wager.single", {"wager": wager})
        else:
            return response.redirect("/wager")

    def create(self, view: View, request: Request, response: Response):
        # TODO add wager create
        return "create"

    def store(self, request: Request, response: Response):
        # TODO add wager store
        return "hello"
