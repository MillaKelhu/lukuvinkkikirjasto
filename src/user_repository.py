import hashlib
from os import X_OK

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
        password-kentistä.
        Huom. Metodin kutsujan vastuulla on kutsua commit-metodia
        muutosten tallentamiseksi"""

        query = """INSERT INTO Users (username, password)
               VALUES (:username, :password)"""
        self.session.execute(query, {"username": user["username"],
                                     "password": user["password"]})

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
        password-kentät.
        Huom. Metodin kutsujan
        vastuulla on kutsua commit-metodia muutosten tallentamiseksi"""

        query = """UPDATE Users SET username = :username,
               password = :password WHERE id = :id"""
        self.session.execute(query, {"id": user["id"],
                                     "username": user["username"],
                                     "password": user["password"]})

    def commit(self):
        """Kommitoi muutokset tietokantaan"""

        self.session.commit()

    def rollback(self):
        """Peruuta muutokset tietokantaan"""

        self.session.rollback()

    def login(self,user):
        """Hakee käyttäjän tietokannasta Pythonin dictionary-olion
        user perusteella, jolla on kentät username ja password.
        Metodi tarkistaa mikäli käyttäjä on olemassa ja onko
        annettu salasana oikea. Palauttaa käyttäjän tiedot
        sqlalchemy.engine.RowProxy-oliona, mikäli käyttäjää
        ei ole palauttaa virheilmoituksen."""

        query = """SELECT * FROM Users WHERE username=:username"""
        result = self.session.execute(query, {"username":user["username"]}).fetchone()
        
        if result == None or self.check_password_hash(user["password"],result["password"]) == False:
            return "Virheellinen käyttäjänimi tai salasana."
        return result

    def register(self,user):
        """Metodi, joka vastaanottaa Pythonin dictionary-olion,
        jolla on kentät username ja password. Metodi tarkastaa
        onko käyttäjänimi jo käytössä, jos ei ole se kutsuu
        metodia create hashattyään salasanan, jonka jälkeen
        committaa muutoksen tietokantaan. Mikäli käyttäjänimi
        on käytössä metodi palauttaa False."""

        salted_password = user["password"] + \
            "joiafhoufheoa3ijfla3dfnuneugyugeoj830803"
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
        user["password"] = hashed_password

        try:
            self.create(user)
            self.commit()
            return True
        except Exception:
            return False

    def check_password_hash(self,input_password,db_password):
        """Metodi tarkastaa vastaako annettu salasana 
        tietokannassa olevaa salasanaa"""

        input_password = input_password + \
            "joiafhoufheoa3ijfla3dfnuneugyugeoj830803"
        input_password = hashlib.sha256(input_password.encode()).hexdigest()
        return input_password == db_password

