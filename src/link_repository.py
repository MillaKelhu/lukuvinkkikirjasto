from sqlalchemy.orm import session

class LinkRepository:
    """Konstruktoi sqlalchemy-sessiosta linkki-repositorion"""
    def __init__(self, session):
        self.session = session

    """Hakee linkin tietokannasta Pythonin dictionary-olion id-kentän
    perusteella ja palauttaa kyseisen rivin
    sqlalchemy.engine.RowProxy-oliona"""
    def find(self, link):
        q = "SELECT * FROM Links WHERE id = :id"
        return self.session.execute(q, {"id": link["id"]}).fetchone()

    """Hakeee kaikki linkit tietokannasta ja palauttaa ne listana
    sqlalchemy.engine.RowProxy-olioita"""
    def find_all(self):
        return self.session.execute("SELECT * FROM Links").fetchall()

    """Luo linkki tietokantaan Pythonin dictionary-olion title- ja
    link_url-kentistä.

    Huom. Metodin kutsujan vastuulla on kutsua commit-metodia
    muutosten tallentamiseksi"""
    def create(self, link):
        q = """INSERT INTO Links (title, link_url, created_at)
               VALUES (:title, :link_url, datetime('now'))"""
        self.session.execute(q, {"title": link["title"],
                                 "link_url": link["link_url"]})

    """Hae linkki tietokannasta Pythonin dictionary-olion id-kentän
    perusteella ja poista kyseinen rivi.

    Metodin kutsujan vastuulla on kutsua commit-metodia muutosten
    tallentamiseksi"""
    def delete(self, link):
        q = "DELETE FROM Links WHERE id = :id"
        self.session.execute(q, {"id": link["id"]})

    """Hae linkki tietokannasta Pythonin dictionary-olion id-kentän
    perusteella ja päivitä sen title- ja link_url-kentät.

    Metodin kutsujan vastuulla on kutsua commit-metodia muutosten
    tallentamiseksi"""
    def update(self, link):
        q = """UPDATE Links SET title = :title,
               link_url = :link_url WHERE id = :id"""
        self.session.execute(q, {"id": link["id"],
                                 "title": link["title"] ,
                                 "link_url": link["link_url"]})

    """Kommitoi muutokset tietokantaan"""
    def commit(self):
        self.session.commit()

    """Peruuta muutokset tietokantaan"""
    def rollback(self):
        self.session.rollback()
