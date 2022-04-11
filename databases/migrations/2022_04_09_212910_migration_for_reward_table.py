"""MigrationForRewardTable Migration."""

from masoniteorm.migrations import Migration



class MigrationForRewardTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("rewards") as table:
            table.increments("id")
            table.unsigned_integer("wager_id")
            table.long_text("description")
            table.integer("amount").nullable()

            table.foreign("wager_id").references("id").on("wagers").on_delete("cascade") 
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("rewards")
