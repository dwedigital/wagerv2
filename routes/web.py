from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show").name('home'),
    Route.group(
        [
            Route.get("/", "WagerController@index").name('index'),
            Route.get("/create", "WagerController@create").name('create'),
            Route.get("/@id:int", "WagerController@wager").name('single'),
            Route.post("/create", "WagerController@store").name('store'),
            
        ], prefix="/wager", middleware=['auth'], name="wager"
    ),Route.get('wager/accept/@token', 'WagerController@accept').name('wager.accept'),
    Route.get('wager/decline/@token', 'WagerController@decline').name('wager.decline'),
    ]
ROUTES+= Auth.routes()