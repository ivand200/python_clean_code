class Connector:
    def __init__(self, source):
        self.source = source
        self._timeout = 60

conn = Connector("postgresql://localhost")
print(conn.source)
print(conn._timeout)