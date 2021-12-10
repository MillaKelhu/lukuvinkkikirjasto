import os
import unittest
from link_repository import LinkRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestLinkRepository(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        dbpath = os.path.join(dirname, "test.db")
        engine = create_engine(f"sqlite:///{dbpath}")
        Session = sessionmaker()
        Session.configure(bind=engine)
        session = Session()

        self.link_repository = LinkRepository(session)

    def tearDown(self):
        pass

    def test_find_all(self):
        result = self.link_repository.find_all()

        self.assertEqual(len(result), 3)

    def test_create(self):
        link = {"title": "Wheeler Graph",
                "link_url": "https://www.sciencedirect.com/science/article/pii/S0304397517305285",
                "created_by": 1}

        self.link_repository.create(link)
        result = self.link_repository.find_all()
        self.assertEqual(len(result), 4)

        self.link_repository.rollback()

    def test_delete(self):
        link = {"id": 1}

        self.link_repository.delete(link)

        result = self.link_repository.find_all()

        self.assertEqual(len(result), 2)

        self.link_repository.rollback()

    def test_update(self):
        link = {"id": 2, "title": "Apache Spark",
                "link_url": "https://spark.apache.org/"}

        result = self.link_repository.find(link)

        self.assertEqual(result[1], "Spark")

        result = self.link_repository.update(link)

        self.assertEqual(result[1], "Apache Spark")

        self.link_repository.rollback()

    def test_find(self):
        link = {"id": 2}
        result = self.link_repository.find(link)

        self.assertEqual(result[1], "Spark")
        self.assertEqual(result[2], "https://spark.apache.org/")
