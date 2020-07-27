import sqlite3
from time import time


class Data:
    def __init__(self):
        self.connection = sqlite3.connect('data.db', check_same_thread=False)

    def create(self, api, question, answer):
        sql = 'INSERT INTO drills (api, question, answer, start_time) values ("{}", "{}", {}, "{}")'.format(
            api, question, answer, time())
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        return cursor.lastrowid

    def find_by_id(self, drill_id):
        sql = 'SELECT * FROM drills WHERE drill_id = {}'.format(drill_id)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        return result

    def finsh(self, drill_id, stop_time, elapsed):
        sql = 'UPDATE drills SET stop_time = "{}", elapsed = {} WHERE drill_id = {}'.format(
            stop_time, elapsed, drill_id)
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
