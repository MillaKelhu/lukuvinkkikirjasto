import unittest
from user_repository import UserRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestLinkRepository(unittest.TestCase):
    def setUp(self):
        engine = create_engine(f"postgresql+psycopg2://localhost/")
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
                "password": "another_good_password"
                }

        self.user_repository.create(user)
        result = self.user_repository.find_all()
        self.assertEqual(len(result), 2)

        self.user_repository.rollback()

    def test_delete(self):
        user = {"username": "user_two",
                "password": "another_good_password"
                }

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
                "password": "better_password"
                }

        result = self.user_repository.find(user)

        self.assertEqual(result["password"], "good_password")

        result = self.user_repository.update(user)

        self.assertEqual(result["password"], "better_password")

        self.user_repository.rollback()

    def test_find(self):
        user = {"id": 1}
        result = self.user_repository.find(user)

        self.assertEqual(result[1], "user_one")
