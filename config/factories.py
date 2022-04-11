from masoniteorm import Factory
from app.models.User import User

def user_factory(faker):
    return {
        'name': faker.name(),
        'email': faker.email(),
        'password': 'secret'
    }

Factory.register(User, user_factory)