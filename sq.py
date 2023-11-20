import MySQLdb

db = MySQLdb.connect(user=uname, password=pwd, database=db_name)
cursor = db.cursor()
cursor.execute(
    """
    SELECT name FROM cities
    WHERE state_id =
        (
            SELECT id FROM states
            WHERE name=%s
        )
    """,
    (state,)
)