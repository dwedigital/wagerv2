"""MigrationForWagersTable Migration."""

from masoniteorm.migrations import Migration


class MigrationForWagersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("wagers") as table:
            table.increments("id")
            table.text("name")
            table.long_text("description")
            table.text("challenger")
            table.text("proposer")
            table.text("referee").nullable()

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("wagers")
