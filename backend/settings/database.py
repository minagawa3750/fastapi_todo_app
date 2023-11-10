from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm import declarative_base
from settings.env import Env

_database_url = URL.create(
    drivername="mysql+pymysql",
    username=Env.MYSQL_USER,
    password=Env.MYSQL_PASSWORD,
    host=Env.MYSQL_HOST,
    database=Env.MYSQL_DATABASE,
)

Engine = create_engine(_database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=Engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
