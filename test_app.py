
import os
import unittest
import tempfile
from main import login, CONFIG_PATH

class DummyEntry:
    def __init__(self, text):
        self.text = text

    def get(self):
        return self.text

class TestLogin(unittest.TestCase):
    def setUp(self):
        global entry_user, entry_pass
        entry_user = DummyEntry("admin")
        entry_pass = DummyEntry("password")

        os.environ["APPDATA"] = tempfile.gettempdir()

        if os.path.exists(CONFIG_PATH):
            os.remove(CONFIG_PATH)

    def test_login_success(self):
        try:
            login()
        except Exception as e:
            self.fail(f"Login raised an exception: {e}")
