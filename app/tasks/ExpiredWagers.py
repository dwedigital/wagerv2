"""Task Module Description"""
from masonite.scheduling import Task
from masonite.facades import Mail
from app.mailables.WagerExpired import WagerExpired
from app.mailables.WagerExpiredRef import WagerExpiredRef

from app.models.Wager import Wager
from app.models.Message import Message


class ExpiredWagers(Task):
    def handle(self):
        wagers = Wager.all()
        for wager in wagers:
            # Check wager has epired and has not already had an expired message sent before
            if wager.expired() and not wager.messages.contains("message_status_id",5):  
                # If wager has a referee then ask referee for outcome instead of participants             
                if wager.referee:
                    print("Sending expired wager to referee")
                    Mail.mailable(WagerExpiredRef(wager).to(wager.referee)).send()
                    # Add message to wager to say referee has been aseked for outomce
                    Message.create({"wager_id": wager.id, "message_status_id": 6})
                    
                else:
                    # Send expired wager to participants if no referee
                    print(f"Wager {wager.id} has expired and no referee")
                    Mail.mailable(WagerExpired(wager).to(wager.proposer)).send()
                    Mail.mailable(WagerExpired(wager).to(wager.challenger)).send()
                # Add message to wager saying wager has expired
                Message.create({"wager_id": wager.id, "message_status_id": 5})
                
                
                
