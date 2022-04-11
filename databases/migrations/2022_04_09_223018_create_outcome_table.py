"""CreateOutcomeTable Migration."""

from masoniteorm.migrations import Migration


class CreateOutcomeTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("outcomes") as table:
            table.increments("id")
            table.unsigned_integer("winner_id")
            table.unsigned_integer("loser_id")
            table.unsigned_integer("wager_id")
            table.foreign("wager_id").references("id").on("wagers").on_delete("cascade")
            table.foreign("winner_id").references("id").on("users").on_delete("cascade")
            table.foreign("loser_id").references("id").on("users").on_delete("cascade")

            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("Outcomes")
