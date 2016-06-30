from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String, ForeignKey, Table

from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

# Connect to postgres server.
engine = create_engine('postgresql://postgres:123456@localhost:5432/Downloader')

# Declare ORM Mapping
Base = declarative_base()

# Create Session
Sess = sessionmaker(bind=engine)
session = Sess()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key= True)
	username = Column(String, unique=True)
	fullname = Column(String)
	password = Column(String)

	def __repr__(self):
		return "name {0} fullname {1} password {2}".format(self.username,
															self.fullname,
															self.password)

# Asso table

association_table = Table('asso', Base.metadata,
	Column('left_id', Integer, ForeignKey('tags.id')),
	Column('right_id', Integer, ForeignKey('dir.id'))
	)

class Tags(Base):
	__tablename__ = 'tags'

	id = Column(Integer, primary_key=True)
	tag = Column(String)
	vid_name = relationship(
		'Dir',
		secondary=association_table,
		back_populates='tag_name'
		)

class Dir(Base):
	__tablename__ = 'dir'

	id = Column(Integer, primary_key=True)
	name = Column(Integer, unique=True)
	link = Column(Integer)
	tag_name = relationship(
		'Tags',
		secondary=association_table,
		back_populates='vid_name'
		)

def create_db():
	Base.metadata.create_all(engine)

def teardown_db():
	Base.metadata.drop_all(engine)

teardown_db()
print "Deleted"
create_db()