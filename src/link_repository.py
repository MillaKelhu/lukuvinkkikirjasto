class LinkRepository:
    def __init__(self, session):
        """Konstruktoi sqlalchemy-sessiosta linkki-repositorion"""

        self.session = session

    def find(self, link):
        """Hakee linkin tietokannasta Pythonin dictionary-olion id-kentän
        perusteella ja palauttaa kyseisen rivin
        sqlalchemy.engine.RowProxy-oliona"""

        query = "SELECT * FROM Links WHERE id = :id"

        return self.session.execute(query, {"id": link["id"]}).fetchone()

    def find_all(self):
        """Hakee kaikki linkit tietokannasta ja palauttaa ne listana
        sqlalchemy.engine.RowProxy-olioita"""

        return self.session.execute("SELECT * FROM Links").fetchall()

    def create(self, link):
        """Luo linkki tietokantaan Pythonin dictionary-olion title- ja
        link_url-kentistä.
        Huom. Metodin kutsujan vastuulla on kutsua commit-metodia
        muutosten tallentamiseksi"""

        query = """INSERT INTO Links (title, link_url, created_at, created_by)
               VALUES (:title, :link_url, datetime('now'), :created_by)"""
        self.session.execute(query, {"title": link["title"],
                                     "link_url": link["link_url"],
                                     "created_by": link["created_by"]}
                             )

    def delete(self, link):
        """Hae linkki tietokannasta Pythonin dictionary-olion id-kentän
        perusteella ja poista kyseinen rivi.
        Huom. Metodin kutsujan vastuulla on kutsua commit-metodia muutosten
        tallentamiseksi"""

        query = "DELETE FROM Links WHERE id = :id"
        self.session.execute(query, {"id": link["id"]})

    def delete_by_title_and_url(self, link):
        """Hae linkki tietokannasta Pythonin dictionary-olion title- ja link_url-kentän
        perusteella ja poista kyseinen rivi.
        Huom. Metodin kutsujan vastuulla on kutsua commit-metodia muutosten
        tallentamiseksi
        Huom. Älä käytä metodia varsinaisessa ohjelmassa, vaan pelkästään robot-testeissä"""

        query = "DELETE FROM Links WHERE title = :title AND link_url = :link_url"
        self.session.execute(
            query, {"title": link["title"], "link_url": link["link_url"]})

    def update(self, link):
        """Hae linkki tietokannasta Pythonin dictionary-olion
        id-kentän perusteella ja päivitä sen title- ja
        link_url-kentät.
        Huom. Metodin kutsujan
        vastuulla on kutsua commit-metodia muutosten tallentamiseksi"""

        query = """UPDATE Links SET title = :title,
               link_url = :link_url WHERE id = :id"""
        return self.session.execute(query, {"id": link["id"],
                                    "title": link["title"],
                                            "link_url": link["link_url"]}
                                    )

    def commit(self):
        """Kommitoi muutokset tietokantaan"""

        self.session.commit()

    def rollback(self):
        """Peruuta muutokset tietokantaan"""

        self.session.rollback()
