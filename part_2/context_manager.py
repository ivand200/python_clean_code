import os


def stop_database():
    print("systemctl stop postgresql.service")
    # os.system("systemctl stop postgresql.service")
    # run("systemctl stop postgresql.service")


def start_database():
    print("systemctl start postgresql.service")
    # os.system("systemctl start postgresql.service")
    # run("systemctl start postgresql.service")


class DBhandler:
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()


def db_backup():
    print("pg_dump database")
    # os.system("pg_dump database")


def main():
    with DBhandler():
        db_backup()


if __name__ == "__main__":
    main()