from raw.DB_CONNECT import DBConnect
from connection import DB_CONNECTION

db = DBConnect(**DB_CONNECTION)

def _add_cursor_wrapper(func):
    def wrapper(*args, **kwargs):
        with db.get_connection().cursor() as cur:
            return func(cur, *args, **kwargs)

    return wrapper

class Requests:
        @staticmethod
        @_add_cursor_wrapper
        def get_all_stores(cur):
            cur.execute(
                '''
                SELECT *
                FROM musicstores
                '''
            )
            fetch = cur.fetchall()
            if fetch is None:
                return 'Данные отсутсвуют'
            else:
                return fetch

        @staticmethod
        @_add_cursor_wrapper
        def get_all_vinyl(cur):
            cur.execute(
                '''
                SELECT *
                FROM vinyl
                '''
            )
            fetch = cur.fetchall()
            if fetch is None:
                return 'Винил не добавлен в базу данных'
            else:
                return fetch

        @staticmethod
        @_add_cursor_wrapper
        def get_music_store_by_name(cur, music_store_name):
            cur.execute(
                '''
                SELECT id, name, address FROM musicstores
                WHERE name = %s
                ''',
                (music_store_name,)
            )
            fetch = cur.fetchone()
            if fetch is None:
                return 'Такого магазина нет в нашей базе данных'
            else:
                return fetch

        @staticmethod
        @_add_cursor_wrapper
        def get_music_store_by_address(cur, music_store_address):
            cur.execute(
                '''
                SELECT id, name, address FROM musicstores
                WHERE address = %s
                ''',
                (music_store_address,)
            )
            fetch = cur.fetchone()
            if fetch is None:
                return 'По данному адресу найти магазин не удалось'
            else:
                return fetch

        @staticmethod
        @_add_cursor_wrapper
        def get_vinyl_by_title(cur, vinyl_title):
            cur.execute(
                '''
                SELECT id, title, author_name, year FROM vinyl
                WHERE title = %s
                ''',
                (vinyl_title,)
            )
            fetch = cur.fetchone()
            if fetch is None:
                return 'Такой пластинки найти не удалось'
            else:
                return fetch

        @staticmethod
        @_add_cursor_wrapper
        def add_store(cur, name, address):
            cur.execute(
                '''
                INSERT INTO musicstores (name, address)
                VALUES (%s, %s)
                ''',
                (name, address,)
            )
            return 'Магазин был добавлен'
        @staticmethod
        @_add_cursor_wrapper
        def add_vinyl(cur, title, author_name, store_id, year):
            cur.execute(
                '''
                INSERT INTO vinyl (title, author_name, store_id, year)
                VALUES (%s, %s, %s, %s)
                ''',
                (title, author_name, store_id, year,)
            )
            return 'Пластинка была добавлена'

        @staticmethod
        @_add_cursor_wrapper
        def find_store_by_vinyl(cur, title):
            cur.execute(
                '''
                SELECT musicstores.name, musicstores.address
                FROM musicstores
                INNER JOIN vinyl
                ON vinyl.store_id = musicstores.id
                WHERE vinyl.title = %s      
                ''',
                (title,)
            )
            fetch = cur.fetchone()
            if fetch is None:
                return 'Не удалось найти данную пластинку'
            else:
                return fetch

        @staticmethod
        @_add_cursor_wrapper
        def get_all_stores_vinyl(cur, name):
            cur.execute(
                '''
                SELECT vinyl.title, vinyl.author_name, vinyl.year
                FROM musicstores
                INNER JOIN vinyl
                ON vinyl.store_id = musicstores.id
                WHERE musicstores.name = %s
                ''',
                (name,)
            )
            fetch = cur.fetchall()
            if fetch is None:
                return 'В данном магазине нет пластинок в наличии'
            else:
                return fetch


# print(get_music_store_by_name('Мир Винила'))
# print(get_music_store_by_address('Жуков пр., 21Б'))
# print(get_vinyl_by_title('Korn'))
# print(add_store('Музторг', 'Московская 151/247'))
# print(add_vinyl('Горгород', 'Oxxxymiron', '2', '2015'))
# print(find_store_by_vinyl('Река крови'))
# print(get_all_stores_vinyl('Это винил'))
# print(get_all_stores())
# print(get_all_vinyl())