from db import set_session
from tables import MusicStores, Vinyl

class AlchemyBack():

    @staticmethod
    def get_all_stores():
        with set_session() as session:
            return session.query(
                MusicStores.id, MusicStores.name, MusicStores.address
            ).all()

    @staticmethod
    def get_all_vinyl():
        with set_session() as session:
            return session.query(
                Vinyl.id, Vinyl.title, Vinyl.author_name, Vinyl.store_id, Vinyl.year
            ).all()

    @staticmethod
    def get_music_store_by_name(name):
        with set_session() as session:
            return session.query(
                MusicStores.id, MusicStores.name, MusicStores.address
            ).filter_by(name=name).all()

    @staticmethod
    def get_music_store_by_address(address):
        with set_session() as session:
            return session.query(
                MusicStores.id, MusicStores.name,MusicStores.address
            ).filter_by(address=address).all()

    @staticmethod
    def get_vinyl_by_title(title):
        with set_session() as session:
            return session.query(
                Vinyl.id, Vinyl.title, Vinyl.author_name, Vinyl.store_id, Vinyl.year
            ).filter_by(title=title).all()

    @staticmethod
    def add_store(name, address):
        new_store = MusicStores(
            name=name,
            address=address
        )
        with set_session() as session:
            session.add(new_store)
            return f'Магазин был успешно добавлен'

    @staticmethod
    def add_vinyl(title, author_name, store_id, year):
        vinyl = Vinyl(
            title=title,
            author_name=author_name,
            store_id=store_id,
            year=year
        )
        with set_session() as session:
            session.add(vinyl)
            return f'Винил был успешно добавлен'

# print(AlchemyBack.get_all_vinyl())
# print(AlchemyBack.get_all_stores())
# print(AlchemyBack.get_music_store_by_name('Это винил'))
# print(AlchemyBack.get_music_store_by_address('Чапаева 151/247'))
# print(AlchemyBack.get_vinyl_by_title('Slipknot'))
# print(AlchemyBack.add_store('Большой магазин пластинок', 'Московская 137'))



