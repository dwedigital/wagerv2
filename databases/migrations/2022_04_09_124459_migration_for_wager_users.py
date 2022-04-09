"""MigrationForWagerUsers Migration."""

from masoniteorm.migrations import Migration


class MigrationForWagerUsers(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("wager_user") as table:
            table.unsigned_integer("user_id")
            table.unsigned_integer("wager_id")
            table.foreign('user_id').references('id').on('users').on_delete('cascade')
            table.foreign('wager_id').references('id').on('wagers').on_delete('cascade')
            table.primary(['user_id', 'wager_id'])
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("wager_user")
