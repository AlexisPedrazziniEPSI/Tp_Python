class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = {}
            self.initialized = True

    def create_context(self): #
        return DatabaseContext(self)

class DatabaseContext:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.operations = []

    def add_entry(self, entry_id, data):
        self.db_connection.data[entry_id] = data

    def delete_entry(self, entry_id):
        if entry_id in self.db_connection.data:
            del self.db_connection.data[entry_id]

    def drop_all(self):
        self.db_connection.data.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


db = DatabaseConnection()

with db.create_context() as based:
    based.add_entry(1, "data1")
    based.add_entry(2, "data2")
    based.delete_entry(1)

assert db.data == {2: 'data2'}

with db.create_context() as based:
    based.drop_all()

assert db.data == {}