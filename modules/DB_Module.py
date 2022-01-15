import os
import sqlite3


class MPADatabase(object):
    database_file = None
    connection = None

    def __init__(self, database_file):
        self.database_file = database_file
        self.create_database_if_not_exist()

    def create_database_if_not_exist(self):
        self.connection = sqlite3.connect(self.database_file)
