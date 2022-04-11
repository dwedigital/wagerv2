from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from app.models.User import User
from app.models.Wager import Wager
from app.models.Reward import Reward
from masonite.mail import Mail
from app.mailables.NewChallenge import NewChallenge


class WagerController(Controller):
    def index(self, view: View):
        return view.render("wager.home")

    def wager(self, view: View, request: Request, response: Response):
        wager = Wager.find(request.param("id"))
        if wager:
            return view.render("wager.single", {"wager": wager})
        else:
            # TODO fix this up so it just says "wager not found"
            return response.redirect("/wager")

    def create(self, view: View, request: Request, response: Response):
        return view.render("wager.create")

    def store(self, request: Request, response: Response, mail: Mail):
        # Create the wager from the form data
        Wager.create(
            {
                "name": request.input("name"),
                "description": request.input("description"),
                "proposer": request.input("proposer"),
                "challenger": request.input("challenger"),
                "referee": request.input("referee"),
                "expiry_date": request.input("expiry-date"),
            }
        )
        # If the user does not exist then create one with just their email so they can sign up
        if User.where("email", request.input("challenger")).first() == None:
            User.create(
                {
                    "email": request.input("challenger"),
                }
            )
        # Email the challenger with a new challenge email
        mail.mailable(NewChallenge().to(request.input("challenger"))).send()
        return "hello"
