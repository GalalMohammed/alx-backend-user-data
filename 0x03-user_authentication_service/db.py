#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save the user to the database.
        """
        row = User(email=email, hashed_password=hashed_password)
        self._session.add(row)
        self._session.commit()
        return row

    def find_user_by(self, **kwargs: object) -> User:
        """Find a user in the database based on keyword arguments.
        """
        row = self._session.query(User).filter_by(**kwargs).first()
        if not row:
            raise NoResultFound
        return row
