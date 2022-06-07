"""CreateMessageStatusTable Migration."""

from masoniteorm.migrations import Migration


class CreateMessageStatusTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("message_statuses") as table:
            table.integer("id")
            table.char("status", length=250)
            table.timestamps()
            table.primary("id")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("message_statuses")
