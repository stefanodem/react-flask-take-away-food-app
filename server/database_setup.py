import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create Base from which DB classes inherit
Base = declarative_base()

class Chef(Base):
    __tablename__ = 'chef'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    name = Column(String(20), nullable=False)
    description = Column(String(250))
    price = Column(Integer)
    image_url = Column(String(80))
    chef_id = Column(Integer, ForeignKey('chef.id'))
    chef = relationship(Chef)

    # Define JSON output structure
    @property
    def serialize(self):
        return {
            'date': self.date,
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'image': self.image_url,
        }

engine = create_engine('sqlite:///foodapp.db')

Base.metadata.create_all(engine)
