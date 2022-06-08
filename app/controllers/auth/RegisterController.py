from masonite.authentication import Auth
from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from app.models.User import User
from masonite.sessions import Session


class RegisterController(Controller):
    def show(self, view: View):  # Show register page
        return view.render("auth.register")

    def store(self, auth: Auth, request: Request, response: Response,session:Session) :  # store register user
        errors = request.validate(
            {
                "email": "required",
                "name": "required",
                "password": "required|confirmed",
            }
        )

        if errors:
            return response.back().with_errors(errors)
        
        if bool(User.where('email','user@example.com')):
            return response.redirect("/register").with_errors("User already exists")

        user = auth.register(request.only("name", "email", "password"))

        if not user:
            return response.redirect("/register")

        return response.redirect("/home")
