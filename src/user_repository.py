class UserRepository:
    def __init__(self, session):
        """Konstruktoi sqlalchemy-sessiosta linkki-repositorion"""

        self.session = session

    def find(self, user):
        """Hakee käyttäjän tietokannasta Pythonin dictionary-olion id-kentän
        perusteella ja palauttaa kyseisen rivin
        sqlalchemy.engine.RowProxy-oliona"""

        query = "SELECT * FROM Users WHERE id = :id"

        return self.session.execute(query, {"id": user["id"]}).fetchone()

    def find_all(self):
        """Hakeee kaikki käyttäjät tietokannasta ja palauttaa ne listana
        sqlalchemy.engine.RowProxy-olioita"""

        return self.session.execute("SELECT * FROM Users").fetchall()

    def create(self, user):
        """Luo käyttäjä tietokantaan Pythonin dictionary-olion username- ja
        password-kentistä. Palauttaa luodun rivin
        sqlalchemy.engine.RowProxy-oliona.
        Huom. Metodin kutsujan vastuulla on kutsua commit-metodia
        muutosten tallentamiseksi"""

        query = """INSERT INTO Users (username, password)
               VALUES (:username, :password) RETURNING *"""
        return self.session.execute(query, {"username": user["username"],
                                            "password": user["password"]}
                                    ).fetchone()

    def delete(self, user):
        """Hae käyttäjä tietokannasta Pythonin dictionary-olion id-kentän
        perusteella ja poista kyseinen rivi.
        Huom. Metodin kutsujan vastuulla on kutsua commit-metodia muutosten
        tallentamiseksi"""

        query = "DELETE FROM Users WHERE id = :id"
        self.session.execute(query, {"id": user["id"]})

    def update(self, user):
        """Hae käyttäjä tietokannasta Pythonin dictionary-olion
        id-kentän perusteella ja päivitä sen username- ja
        password-kentät. Palauttaa muokatun rivin
        sqlalchemy.engine.RowProxy-oliona. Huom. Metodin kutsujan
        vastuulla on kutsua commit-metodia muutosten tallentamiseksi"""

        query = """UPDATE Users SET username = :username,
               password = :password WHERE id = :id RETURNING *"""
        return self.session.execute(query, {"id": user["id"],
                                    "username": user["username"],
                                            "password": user["password"]}).fetchone()

    def commit(self):
        """Kommitoi muutokset tietokantaan"""

        self.session.commit()

    def rollback(self):
        """Peruuta muutokset tietokantaan"""

        self.session.rollback()
