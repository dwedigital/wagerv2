"""Base Database Seeder Module."""
from masoniteorm.seeds import Seeder

from .outcome_table_seeder import OutcomeTableSeeder
from .reward_table_seeder import RewardTableSeeder
from .user_table_seeder import UserTableSeeder
from .wager_table_seeder import WagerTableSeeder
from .message_status_table_seeder import MessageStatusTableSeeder


class DatabaseSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        self.call(UserTableSeeder)
        self.call(WagerTableSeeder)
        self.call(RewardTableSeeder)
        self.call(OutcomeTableSeeder)
        self.call(MessageStatusTableSeeder)
