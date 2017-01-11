from selenium import webdriver
import unittest

chromedriver = "/usr/bin/chromedriver"

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_and_retrieve_it_later(self):
        # User first check out the homepage of to-do app
        self.browser.get('http://localhost:8000')

        # He notices browser title and header mention To-Do
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish Test!')

if __name__ == '__main__':
    unittest.main()
