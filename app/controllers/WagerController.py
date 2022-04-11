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
            return view.render("wager.home")

    def store(self, request: Request, response: Response):
        #TODO add wager store
        return "hello"
        

    def wager(self, view: View, request: Request, response: Response):
        #TODO add wager wager
        wager= Wager.find(request.param("id"))
        if(wager):
            return view.render("wager.single",{
                "wager": wager
            })
        else:
            return response.redirect("/wager")
            
        
