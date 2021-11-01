from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
        __tablename__ = 'pessoas'
        
        id = Column(Integer, primary_key=True)
        nome = Column(String)
        idade = Column(Integer)

        def __repr__(self):
            return f'Pessoa(nome={self.nome}, idade={self.idade})'      

Base.metadata.create_all(engine)

# p1 = Pessoa(nome= 'Fauto')
# p2 = Pessoa(nome= 'Fabio')
# p3 = Pessoa(nome= 'Gustavo')
# p4 = Pessoa(nome= 'JP')
# p5 = Pessoa(nome= 'Luiza')
# p6 = Pessoa(nome= 'Elaine')

p1 = Pessoa(nome= 'Eduardo', idade='27')
p2 = Pessoa(nome= 'Carlos', idade= '55')
p3 = Pessoa(nome= 'Elaine', idade='33')

session.add(p1)
session.add(p2)
session.add(p3)
# session.add_all([p2, p3, p4, p5])

session.commit()


from pprint import pprint

pprint(session.query(Pessoa).all())