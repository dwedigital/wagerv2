"""OutcomeTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.models.Outcome import Outcome


class OutcomeTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Outcome.create({
            "winner_id": 1,
            "loser_id": 2,
            "wager_id": 1,
        })

   
