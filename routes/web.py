from masonite.authentication import Auth
from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show").name('home'),
    Route.group(
        [
            Route.get("/", "WagerController@index").name('index'),
            Route.get("/create", "WagerController@create").name('create'),
            Route.get("/@id:int", "WagerController@wager").name('single'),
            Route.post("/create", "WagerController@store").name('store'),
            
        ], prefix="/wager", middleware=['auth'], name="wager"
    ),Route.get('wager/@token/accept', 'WagerController@accept').name('wager.accept'),
    Route.get('wager/@token/decline', 'WagerController@decline').name('wager.decline'),
    
    Route.group(
        [
        Route.get("/", "AccountController@show").name('index'),
    ],prefix="/account", middleware=['auth'], name="account"
        ),
    
    ]
ROUTES+= Auth.routes()