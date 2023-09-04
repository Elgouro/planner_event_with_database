from sqlmodel import  SQLModel, Session, create_engine
from models.event import Event

database_connection_string = "sqlite:///database/planner.db"
connect_args = {"check_same_thread":False}
engine_url =  create_engine(database_connection_string, echo=True, connect_args=connect_args)
#definition de la fonction de connexion
def conn():
    SQLModel.metadata.create_all(engine_url)
def get_session():
    with Session(engine_url) as session:
        yield session