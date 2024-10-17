from sqlalchemy import Column, Integer, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class MusicStores(Base):

    __tablename__ = 'musicstores'

    id = Column(Integer, primary_key=True)
    name = Column(CHAR(length=100), nullable=False)
    address = Column(CHAR(length=100), nullable=False)

    vinyl = relationship('Vinyl', back_populates='musicstores')


class Vinyl(Base):

    __tablename__ = 'vinyl'

    id = Column(Integer, primary_key=True)
    title = Column(CHAR(length=150), nullable=False)
    author_name = Column(CHAR(length=150), nullable=False)
    store_id = Column(Integer, nullable=False)
    year = Column(Integer, ForeignKey(MusicStores.id), nullable=False)

    musicstores = relationship('MusicStores', back_populates='vinyl')
