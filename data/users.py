import sqlalchemy
from data.db_session import SqlAlchemyBase
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    def __init__(self, *args):
        self.surname = args[0]
        self.name = args[1]
        self.age = args[2]
        self.position = args[3]
        self.speciality = args[4]
        self.address = args[5]
        self.email = args[6]

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True, index=True)
    # email = sqlalchemy.Column(sqlalchemy.String,
    #                           index=True, unique=True, nullable=True)
    # hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default=datetime.datetime.now)
    jobs = orm.relationship("Jobs", back_populates='user')
