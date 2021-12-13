from routes import USER_REPOSITORY, session

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"
        self.USER_REPOSITORY = USER_REPOSITORY

    def reset_adding_user(self, username, password):
        self.USER_REPOSITORY.delete_by_username_and_password({"username": username, "password": password})
