import pandas as pd
import requests
from sqlalchemy import create_engine


def db_engine(password, user, host, databse):
    """
    Takes database credentials and creates a database engine using SQL Alchemy
    :param password: Str. Database login password
    :param user: Str. Databse username
    :param host: Str. Hostname
    :param databse: Str. Database to connect
    :return: Returns database engine
    """
    engine = create_engine(f"postgresql://{user}:{password.replace('@','%40')}@{host}/{databse}")
    return engine






