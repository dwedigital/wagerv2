"""MigrationForWagersTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForWagersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("wagers") as table:
            table.increments("wager_id")
            table.text("name")
            table.long_text("description")
            table.integer("challenger_id")
            table.integer("proposer_id")
            table.integer("referee_id")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("wagers")
