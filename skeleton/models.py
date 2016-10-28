# -*- coding: utf-8 -*-

# Skeleton for setting up a basic SQLAlchemy mapping to a SQLite 3 DB
import os
from datetime import datetime

# Define name and path for SQLite3 DB
db_name = "data.db"
db_path = os.path.join(os.getcwd(), db_name)

# Create DB
from sqlalchemy import create_engine
engine = create_engine('sqlite:///' + db_path, echo=False)

# Setup imports
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

# Define Class for Excluded Matter Case Details
from sqlalchemy import Column, Integer, String, Date, Boolean, Text, \
                        ForeignKey

class Base(object):
    """ Extensions to Base class. """
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id =  Column(Integer, primary_key=True)
    
    def as_dict(self):
        """ Return object as a dictionary. """
        temp_dict = {}
        temp_dict['object_type'] = self.__class__.__name__
        for c in self.__table__.columns:
            cur_attr = getattr(self, c.name)
            # If datetime generate string representation
            if isinstance(cur_attr, datetime):
                cur_attr = cur_attr.strftime('%d %B %Y')
            temp_dict[c.name] = cur_attr
        return temp_dict
    
    def populate(self, data):
        """ Populates matching attributes of class instance. 
        param dict data: dict where for each entry key, value equal attributename, attributevalue."""
        for key, value in data.items():
            if hasattr(self, key):
                # Convert string dates into datetimes
                if isinstance(getattr(self, key), datetime) or str(self.__table__.c[key].type) == 'DATE':
                    value = datetime.strptime(value, "%d %B %Y")
                setattr(self, key, value)

Base = declarative_base(cls=Base)

class ParentModel(Base):
    """ Model for a parent entity. """
    # Example name field
    name = Column(String(256))
    
    # Relationship for children
    children = relationship("ChildModel", backref="parent")
    
class ChildModel(Base):
    """ Model for a child entity. """
    # Example name field
    name = Column(String(256))
    
    # Foreign key for parent
    parent_id = Column(Integer, ForeignKey('parentmodel.id'))
    
# Create new DB    
Base.metadata.create_all(engine)

# Setup SQLAlchemy session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)