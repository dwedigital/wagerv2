"""MessageStatusTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.MessageStatus import MessageStatus


class MessageStatusTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        MessageStatus.create({"id":1, "status":"challenge_sent"})
        MessageStatus.create({"id":2, "status":"challenger_accepted"})
        MessageStatus.create({"id":3, "status":"challenge_declined"})
        MessageStatus.create({"id":4, "status":"wager_cancelled_message"})
        MessageStatus.create({"id":5, "status":"wager_expired_message"})
        MessageStatus.create({"id":6, "status":"ref_outcome_requested"})
        MessageStatus.create({"id":7, "status":"ref_declared_outcome"})
        MessageStatus.create({"id":8, "status":"wager_completed"})
        
