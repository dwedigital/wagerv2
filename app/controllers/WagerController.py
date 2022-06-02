import pendulum
from masonite.authentication import Auth
from masonite.controllers import Controller
from masonite.mail import Mail
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from masonite.sessions import Session
from app.models.Reward import Reward
from app.models.User import User
from app.models.Wager import Wager
from app.models.WagerAnalytics import WagerAnalytics
from masonite.broadcasting import Broadcast
from masonite.queues import Queue
from app.jobs.SendNewChallengeEmail import SendNewChallengeEmail
from app.jobs.SendTestEmail import SendTestEmail
from app.mailables.NewChallenge import NewChallenge
class WagerController(Controller):
    def index(self, view: View, auth: Auth, session: Session, broadcast: Broadcast):
        user = auth.user()
        wagers = user.wagers()
        analytics = WagerAnalytics(wagers, auth.user())
        msg = session.get("success")

        # Added this in to test broadcasting
        # broadcast.channel('my-channel','my-event',{"msg": msg})
        return view.render("wager.home", {"wagers": wagers, "analysis": analytics, "msg": msg})

    def wager(self, view: View, request: Request, response: Response):
        wager = Wager.find(request.param("id"))
        if wager and(wager.challenger == request.user().email or wager.proposer == request.user().email or wager.referee == request.user().email):
            return view.render("wager.single", {"wager": wager})
        else:
            # TODO fix this up so it just says "wager not found"
            return response.redirect("/wager")

    def create(self, view: View, request: Request, response: Response, session: Session):
        msg = session.get("error")
        
        return view.render("wager.create", {"msg": msg})

    def store(self, request: Request, response: Response, mail: Mail, session:Session, queue: Queue):
        # Create the wager from the form data
        try:
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
            #mail.mailable(NewChallenge(wager).to(wager.challenger)).send()
            queue.push(SendNewChallengeEmail(wager))
            #queue.push(SendTestEmail("dave@dwedigital.com"))
            return response.redirect("/wager").with_success("Wager successfully created")
        except:
            session.flash("error", "Wager could not be created, please try again and fill in all fields")
            return response.redirect("/wager/create").with_errors("Wager creation failed").with_input()

    def accept(self, view: View, request: Request, response: Response):
        # TODO check wager is not rejected or accepted
        wager = Wager.where("token", request.param("token")).first()
        if(wager.status not in ['declined', 'accepted', 'rejected','complete']):
            wager.update({"status": "accepted"})
            # TODO send email to proposer saying they have accepted the wager
            # TODO fix view to have some meaningful feedback
            return view.render("wager.accept")
        else:
            return view.render("wager.reject")
        

    def decline(self, view: View, request: Request, response: Response):
        # TODO check wager is not rejected or accepted
        wager = Wager.where("token", request.param("token")).first()
        wager.update({"status": "declined"})
        # TODO send email to proposer saying they have rejected the wager
        # TODO fix view to have some meaningful feedback
        return view.render("wager.reject")
    
    def outcome(self, view: View, request: Request, response: Response):
        pass
