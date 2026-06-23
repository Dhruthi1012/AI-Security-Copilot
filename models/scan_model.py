from database.db import get_connection


class ScanModel:

    @staticmethod
    def create_scan(target_id):

        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO scans(target_id)
            VALUES(?)
            """,
            (target_id,)
        )

        connection.commit()

        scan_id = cursor.lastrowid

        connection.close()

        return scan_id

    @staticmethod
    def save_scan_result(
        scan_id,
        port,
        protocol,
        service,
        state
    ):

        connection = get_connection()

        connection.execute(
            """
            INSERT INTO scan_results
            (
                scan_id,
                port,
                protocol,
                service,
                state
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                scan_id,
                port,
                protocol,
                service,
                state
            )
        )

        connection.commit()

        connection.close()

    @staticmethod
    def get_scan_results(scan_id):

        connection = get_connection()

        results = connection.execute(
            """
            SELECT *
            FROM scan_results
            WHERE scan_id = ?
            ORDER BY port
            """,
            (scan_id,)
        ).fetchall()

        connection.close()

        return results

    @staticmethod
    def get_all_scans():

        connection = get_connection()

        scans = connection.execute(
            """
            SELECT
                scans.id,
                scans.scan_date,
                targets.target_name
            FROM scans
            JOIN targets
            ON scans.target_id = targets.id
            ORDER BY scans.id DESC
            """
        ).fetchall()

        connection.close()

        return scans