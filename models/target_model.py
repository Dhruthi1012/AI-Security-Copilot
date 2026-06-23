from database.db import get_connection


class TargetModel:

    @staticmethod
    def add_target(target_name, target_type):

        connection = get_connection()

        connection.execute(
            """
            INSERT INTO targets
            (
                target_name,
                target_type
            )
            VALUES (?, ?)
            """,
            (
                target_name,
                target_type
            )
        )

        connection.commit()
        connection.close()

    @staticmethod
    def get_all_targets():

        connection = get_connection()

        targets = connection.execute(
            """
            SELECT *
            FROM targets
            ORDER BY id DESC
            """
        ).fetchall()

        connection.close()

        return targets

    @staticmethod
    def delete_target(target_id):

        connection = get_connection()

        connection.execute(
            """
            DELETE FROM targets
            WHERE id = ?
            """,
            (target_id,)
        )

        connection.commit()
        connection.close()