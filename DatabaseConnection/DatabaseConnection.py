from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseConnection:
    def __init__(self):
        self.engine = create_engine('sqlite:///database.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def readModel(self, model):
        return self.session.query(model).all()
    def saveModel(self, model):
        self.session.add(model)
        self.session.commit()
        self.session.close()
