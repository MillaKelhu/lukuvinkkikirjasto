import os
import unittest
from link_repository import LinkRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class TestLinkRepository(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.dirname = dirname
        dbpath = os.path.join(dirname, "test.db")
        self.dbpath = dbpath
        schema_path = os.path.join(dirname, "test_schema.sql")
        os.system(f"sqlite3 {dbpath} < {schema_path}")
        self.engine = create_engine(f"sqlite:///{dbpath}")
        Session = sessionmaker()
        Session.configure(bind=self.engine)
        session = Session()

        self.link_repository = LinkRepository(session)

    def tearDown(self):
        self.engine.dispose()
        os.system(f"rm {self.dbpath}")

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

        self.link_repository.update(link)

        result = self.link_repository.find(link)

        self.assertEqual(result[1], "Apache Spark")

        self.link_repository.rollback()

    def test_find(self):
        link = {"id": 2}
        result = self.link_repository.find(link)

        self.assertEqual(result[1], "Spark")
        self.assertEqual(result[2], "https://spark.apache.org/")
