from masonite.broadcasting import CanBroadcast, Channel

class WagerCreated(CanBroadcast):
    channel_name = "my-channel"

    def broadcast_on(self):
        return Channel(self.channel_name)