from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from app.models.User import User
from app.models.Wager import Wager
from app.models.Reward import Reward
from masonite.mail import Mail
from app.mailables.NewChallenge import NewChallenge
from masonite.authentication import Auth
from datetime import datetime
import pendulum
from app.models.WagerAnalytics import WagerAnalytics


class WagerController(Controller):
    def index(self, view: View, auth: Auth):
        user = auth.user()
        wagers = user.wagers()
        analytics = WagerAnalytics(wagers, auth.user())

        return view.render("wager.home", {"wagers": wagers, "analysis": analytics})

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
        print(request.input("expiry-date"))
        wager = Wager.create(
            {
                "name": request.input("name"),
                "description": request.input("description"),
                "proposer": request.input("proposer"),
                "challenger": request.input("challenger"),
                "referee": request.input("referee"),
                "expiry_date": pendulum.parse(request.input("expiry-date")).to_datetime_string(),
            }
        )
        # If the user does not exist then create one with just their email so they can sign up
        if User.where("email", request.input("challenger")).first() == None:
            User.create(
                {
                    "email": request.input("challenger"),
                }
            )

        if request.input("referee") != "":
            if User.where("email", request.input("referee")).first() == None:
                User.create(
                    {
                        "email": request.input("referee"),
                    }
                )

        if request.input("reward-description") != "":
            reward = Reward.create(
                {
                    "description": request.input("reward-description"),
                    "wager_id": wager.id,
                    "reward_type": request.input("reward-type").lower(),
                    "amount": request.input("reward-amount")
                    if request.input("reward-amount") != ""
                    else None,
                }
            )
        # Email the challenger with a new challenge email
        # TODO add wager token as varaible to email fo accept or reject
        mail.mailable(NewChallenge(wager).to(request.input("challenger"))).send()
        return "hello"

    def accept(self, view: View, request: Request, response: Response):
        # TODO check wager is not rejected or accepted
        wager = Wager.where("token", request.param("token")).first()
        wager.update({"status": "accepted"})
        # TODO send email to proposer saying they have accepted the wager
        # TODO fix view to have some meaningful feedback
        return view.render("wager.accept")

    def decline(self, view: View, request: Request, response: Response):
        # TODO check wager is not rejected or accepted
        wager = Wager.where("token", request.param("token")).first()
        wager.update({"status": "declined"})
        # TODO send email to proposer saying they have rejected the wager
        # TODO fix view to have some meaningful feedback
        return view.render("wager.reject")
