"""User Model."""
from masonite.authentication import Authenticates
from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to_many
from masoniteorm.scopes import SoftDeletesMixin


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"

    def wagers(self):
        from app.models.Wager import Wager

        return Wager.where(
            lambda query: (
                query.where("challenger", self.email)
                .or_where("proposer", self.email)
                .or_where("referee", self.email)
            )
        ).get()
