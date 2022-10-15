import contextlib



def stop_database():
    print("systemctl stop postgresql.service")


def start_database():
    print("systemctl start postgresql.service")


def db_backup():
    print("pg_dump database")


@contextlib.contextmanager
def db_handler():
    try:
        stop_database()
        yield
    finally:
        start_database()


with db_handler():
    db_backup()