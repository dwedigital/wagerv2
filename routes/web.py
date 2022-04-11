from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [Route.get("/", "WelcomeController@show").name('home')]
ROUTES+= Auth.routes()