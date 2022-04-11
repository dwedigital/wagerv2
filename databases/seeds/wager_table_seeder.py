"""WagerTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.Wager import Wager


class WagerTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Wager.create({
            "name": "Wager 1",
            "description": "Wager 1 description",
            "challenger_id": 1,
            "proposer_id": 2,
            "referee_id": 3,
        })
        Wager.create({
            "name": "Wager 2",
            "description": "Wager 1 description",
            "challenger_id": 1,
            "proposer_id": 2,
        })
