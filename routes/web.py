from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show").name('home'),
    Route.get("/wager", "WagerController@show").name('wager'),
    Route.post("/wager", "WagerController@store").name('wager.store'),
    Route.get("/wager/@id", "WagerController@wager").name('wager.wager'),
    ]
ROUTES+= Auth.routes()