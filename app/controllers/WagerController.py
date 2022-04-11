from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from app.models.Wager import Wager

class WagerController(Controller):
    def show(self, view: View, request: Request, response: Response):
        if(request.user() == False):
            return response.redirect("/login")
        else:
            #TODO add wager view & form
            print(request.user())
            return "hello"

    def store(self, request: Request, response: Response):
        #TODO add wager store
        return "hello"
        pass

    def wager(self, request: Request, response: Response):
        #TODO add wager wager
        return Wager.find(request.param("id"))
        pass
