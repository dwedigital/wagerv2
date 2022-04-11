"""WagerTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.Wager import Wager


class WagerTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Wager.create({
            "name": "Wager 1",
            "description": "Wager 1 description",
            "challenger": "user@example.com",
            "proposer": "test2@test.com",
            "referee": "test3@test.com",
            "expiry_date": "2020-01-01 00:00:00",
        })
        Wager.create({
            "name": "Wager 2",
            "description": "Wager 1 description",
            "challenger": "user@example.com",
            "proposer": "test2@test.com",
            "expiry_date": "2020-01-01 00:00:00",
        })
