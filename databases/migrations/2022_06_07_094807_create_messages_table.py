"""CreateMessagesTable Migration."""

from masoniteorm.migrations import Migration


class CreateMessagesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("messages") as table:
            table.increments("id")
            table.unsigned_integer("message_status_id")
            table.integer("wager_id")
            table.timestamps()
            
            table.foreign("wager_id").references("id").on("wagers").on_delete("cascade") 
            table.foreign("message_status_id").references("id").on("message_statuses").on_delete("cascade")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("messages")
