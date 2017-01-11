from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        self.assertIn('To Do List', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual('To-Do', header_text)

        # He can also input new to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
            'Enter a to-do item')

        # He now enter new to-do item 'Buy grocery items'
        inputbox.send_keys('Buy grocery items')

        # When he hits enter the page updates and now the page lists
        # "1: Buy grocery items" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
        any(row.text == '1: Buy grocery items' for row in rows),
            "New to-do item did not appear in table --its text was\n%s" % (
                table.text,
            )
        )

        # There is still text inviting him to add new item in to-do list
        # He now enter new to-do item 'Take vegetables'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Take vegetables')
        inputbox.send_keys(Keys.ENTER)

        # When he hits enter the page updates and now the page lists
        # should have 2 items

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy grocery items',[row.text for row in rows])
        self.assertIn('2: Take vegetables', [row.text for row in rows])
        self.fail('Finish Test!')


if __name__ == '__main__':
    unittest.main()
