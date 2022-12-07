from db.ManyToManyMixin import ManyToManyMixin
from db.db import Database


class Papers(Database, ManyToManyMixin):
    pass
