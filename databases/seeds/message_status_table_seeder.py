"""MessageStatusTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.models.MessageStatus import MessageStatus


class MessageStatusTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        MessageStatus.create({"id":1, "message":"challenge_sent"})
        MessageStatus.create({"id":2, "message":"challenger_accepted"})
        MessageStatus.create({"id":3, "message":"challenge_declined"})
        MessageStatus.create({"id":4, "message":"wager_cancelled_message"})
        MessageStatus.create({"id":5, "message":"wager_expired_message"})
        MessageStatus.create({"id":6, "message":"ref_outcome_requested"})
        MessageStatus.create({"id":7, "message":"ref_declared_outcome"})
        MessageStatus.create({"id":8, "message":"wager_completed"})
        
