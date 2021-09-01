import os
import ssl
import pymongo
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()


def connect(db_name="auth_db"):
    """
    Connect to mongodb instance (url) in .env file.

    Parameter
    ----------
    db_name : str
        name of the database to connect

    Returns
    ---------
    db : object
        database client connection object
    """
    db = settings.DBCLIENT[db_name]
    return db


if __name__ == "__main__":
    db = connect()
