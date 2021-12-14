from routes import USER_REPOSITORY
from routes import LINK_REPOSITORY


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.USER_REPOSITORY = USER_REPOSITORY
        self.LINK_REPOSITORY = LINK_REPOSITORY

    def create_user(self, username, password):
        self.USER_REPOSITORY.create(
            {"username": username, "password": password})
        self.USER_REPOSITORY.commit()

    def reset_adding_user(self, username, password):
        self.USER_REPOSITORY.delete_by_username({"username": username})
        self.USER_REPOSITORY.commit()

    def create_link(self, title, url, username, password):
        id = self.USER_REPOSITORY.find_by_login_info(
            {"username": username, "password": password})[0]
        self.LINK_REPOSITORY.create(
            {"title": title, "link_url": url, "created_by": id})
        self.LINK_REPOSITORY.commit()

    def reset_adding_link(self, title, url):
        self.LINK_REPOSITORY.delete_by_title_and_url(
            {"title": title, "link_url": url})
        self.LINK_REPOSITORY.commit()
