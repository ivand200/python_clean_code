"""Good choice"""
import contextlib


def stop_database():
    print("systemctl stop postgresql.service")


def start_database():
    print("systemctl start postgresql.service")


def db_backup():
    print("pg_dump database")


class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
        return self

    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()



@dbhandler_decorator()
def offline_backup():
    print("pg_dump database")



# def offline_backup():
#     with dbhandler_decorator() as handler:
#         pass

if __name__ == "__main__":
    offline_backup()
