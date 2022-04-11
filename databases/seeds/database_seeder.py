"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .user_table_seeder import UserTableSeeder
from .wager_table_seeder import WagerTableSeeder
from .reward_table_seeder import RewardTableSeeder
from .outcome_table_seeder import OutcomeTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)
        self.call(WagerTableSeeder)
        self.call(RewardTableSeeder)
        self.call(OutcomeTableSeeder)
