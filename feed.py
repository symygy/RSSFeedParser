import feedparser
import sqlite3
import schedule
import time
import smtplib
import os

from config import KEY, LOGIN, DATABASE_NAME

class Parser(object):
    feed = feedparser.parse('https://talkpython.fm/episodes/rss')

    def parsed_data(self):
        return [(element.title, element.link) for element in self.feed['entries']]

    def check_if_the_same(self, last_db_row, last_parsed_element):
        data = []
        data.append(last_parsed_element[0])

        if last_db_row[1] != data[0][0]:
            db.insert_data(cur, data)
            return True
        else:
            print("Brak nowych rekordów")
            return False

class Database(object):
    def exists_or_not(self):
        if os.path.isfile(DATABASE_NAME):
            return True
        else:
            return False

    def create_connection(self, db_name):
        connection = sqlite3.connect(db_name)
        return connection

    def create_cursor(self, conn):
        cursor = conn.cursor()
        return cursor

    def close_connection(self, conn):
        try:
            conn.close()
        except Exception as error:
            print(error)

    def create_table(self, cur, conn):
        cur.execute('''CREATE TABLE IF NOT EXISTS {} (id integer primary key asc, title text, link text)'''.format('parser'))

    def insert_data(self, cur, data):
        cur.executemany("INSERT INTO parser VALUES (NULL, ?, ?)", data)

    def get_last_record(self, cur):
        cur.execute("SELECT * FROM parser ORDER BY id DESC LIMIT 1")
        return cur.fetchone()

    def try_to_commit(self, conn):
        try:
            conn.commit()
        except Exception as error:
            print(error)

class Scheduler(object):
    def __init__(self):
        self.db_is_exist = db.exists_or_not()

    def cyclic_job(self):
        data = par.parsed_data()
        reversed_data = data[::-1]

        if self.db_is_exist == False:
            self.db_is_exist = db.exists_or_not()
            db.create_table(cur, conn)
            db.insert_data(cur, reversed_data)
            db.try_to_commit(conn)

        last_db_rec = db.get_last_record(cur)
        job = par.check_if_the_same(last_db_rec, data)
        if job:
            db.try_to_commit(conn)
            sched.email()

    def email(self):
        newest_content = db.get_last_record(cur)
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(LOGIN, KEY)

        smtp_server.sendmail(LOGIN, 'alljunkiesites@gmail.com', 'Subject: Jest nowy odcinek podcastu!\nSiemanko,\n Jest nowy odcinek podcastu. Sprawdz ponizej:'
                                                                '\n Odcinek nr: {} '
                                                                '\n Tytul: {}'
                                                                '\n Link: {}'
                                                                '\n\nPozdrawiam,'
                                                                '\nMichal'.format(newest_content[0],newest_content[1], newest_content[2]))
        smtp_server.quit()
        print('Email sent successfully')

if __name__ == '__main__':

    db = Database()
    par = Parser()
    sched = Scheduler()

    conn = db.create_connection(DATABASE_NAME)
    cur = db.create_cursor(conn)

    #Ustawienie częstotliwości sprawdzania contentu
    schedule.every(1).minutes.do(sched.cyclic_job)

    while True:
        schedule.run_pending()
        time.sleep(1)

    db.close_connection(conn)

