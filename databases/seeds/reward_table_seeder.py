"""RewardTableSeeder Seeder."""

from masoniteorm.seeds import Seeder

from app.models.Reward import Reward


class RewardTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Reward.create({
            "wager_id": 1,
            "description": "Reward 1 description",
            "amount": 100,
            "reward_type":"money"
        })

        Reward.create({
            "wager_id": 2,
            "description": "Reward 2 description",
            "reward_type":"favour"
        })
