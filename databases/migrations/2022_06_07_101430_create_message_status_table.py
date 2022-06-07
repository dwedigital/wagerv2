"""CreateMessageStatusTable Migration."""

from masoniteorm.migrations import Migration


class CreateMessageStatusTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("message_statuses") as table:
            table.integer("id")
            table.char("message", length=250)
            table.primary("id")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("message_statuses")
