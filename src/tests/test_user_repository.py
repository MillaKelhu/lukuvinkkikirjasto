import os
import unittest
from user_repository import UserRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        dbpath = os.path.join(dirname, "test.db")
        engine = create_engine(f"sqlite:///{dbpath}")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        self.user_repository = UserRepository(session)

    def tearDown(self):
        pass

    def test_find_all(self):
        result = self.user_repository.find_all()

        self.assertEqual(len(result), 1)

    def test_create(self):
        user = {"username": "user_two",
                "password": "another_good_password"}

        self.user_repository.create(user)
        result = self.user_repository.find_all()
        self.assertEqual(len(result), 2)

        self.user_repository.rollback()

    def test_delete(self):
        user = {"username": "user_two",
                "password": "another_good_password"}

        self.user_repository.create(user)

        result = self.user_repository.find_all()
        self.assertEqual(len(result), 2)

        self.user_repository.delete(result[1])

        result = self.user_repository.find_all()
        self.assertEqual(len(result), 1)

        self.user_repository.rollback()

    def test_update(self):
        user = {"id": 1,
                "username": "user_one",
                "password": "better_password"}

        result = self.user_repository.find(user)

        self.assertEqual(result["password"], "good_password")

        self.user_repository.update(user)

        result = self.user_repository.find(user)

        self.assertEqual(result["password"], "better_password")

        self.user_repository.rollback()

    def test_find(self):
        user = {"id": 1}
        result = self.user_repository.find(user)

        self.assertEqual(result[1], "user_one")

    def test_register(self):
        user = {"username":"user",
                "password":"pass"}

        value = self.user_repository.register(user)

        self.assertEqual(True,value)

    def test_register_fails_when_username_in_use(self):
        user = {"username":"user",
                "password":"pass"}

        self.user_repository.register(user)
        value = self.user_repository.register(user)

        self.assertEqual(False,value)

    def test_login(self):
        user = {"username":"user",
                "password":"pass"}

        self.user_repository.register(user)
        result = self.user_repository.login(user)

        self.assertEqual(user["username"],result["username"])

    def test_login_with_incorrect_password(self):
        user = {"username":"user",
                "password":"pass"}

        self.user_repository.register(user)
        user["password"] = "sbrölölöö"

        result = self.user_repository.login(user)
        self.assertNotEqual(result["username",user["username"]])
