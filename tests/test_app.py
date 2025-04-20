import os
import unittest
from main import login, CONFIG_PATH

class DummyEntry:
    def __init__(self, text):
        self.text = text
    def get(self):
        return self.text

class TestLogin(unittest.TestCase):
    def setUp(self):
        # Prepare dummy widget entries
        global entry_user, entry_pass
        entry_user = DummyEntry('admin')
        entry_pass = DummyEntry('password')
        # Ensure config file for test
        os.environ['APPDATA'] = '/tmp'
        if os.path.exists(CONFIG_PATH):
            os.remove(CONFIG_PATH)

    def test_login_success(self):
        # Should not raise exception
        try:
            login()
        except:
            self.fail("login() raised exception unexpectedly")

if __name__ == '__main__':
    unittest.main()