from wordlists import URLWordlist
import unittest


class WordlistTests(unittest.TestCase):

    def setUp(self):
        self.test_url = "https://github.com/kzfrb3/namer"
        self.wordlist_under_test = URLWordlist(self.test_url)

    def tearDown(self):
        pass

    def test_url_wordlist_gets_words(self):
        words = self.wordlist_under_test.text
        self.assertTrue(isinstance(words, str))
        self.assertTrue("/>" not in words)
        self.assertTrue("kzfrb3" in words)

    def test_can_pass(self):
        self.assertTrue(True)
