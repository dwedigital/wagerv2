"""MakeUserNameRequired Migration."""

from masoniteorm.migrations import Migration


class MakeUserNameRequired(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.string("name").change()
            table.drop_column('second_password')



    def down(self):
        """
        Revert the migrations.
        """
