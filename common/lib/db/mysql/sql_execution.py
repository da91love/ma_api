import logging

# call instancese
logger = logging.getLogger()

"""
executeSelect function
    :param conn: database connection instance
    :param sql: string
    :param binding: tuple
    :return: tuple. sql result
"""


def executeSql(conn, sql, bindings=None):
    try:
        logger.info('executeSql starts')

        # Create a cursor instance
        cursor = conn.cursor(dictionary=True)

        if bindings:
            sql = sql.format(**bindings)

        logger.info(sql)
        cursor.execute(sql)

        try:
            sql_result = cursor.fetchall()

            # Commit
            conn.commit()

            logger.info('executeSql ends')

            return sql_result
        except BaseException:
            # Commit
            conn.commit()

            logger.info('executeSql ends')
            pass

    except Exception as e:
        conn.rollback()
        raise e
