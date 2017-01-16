from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "/usr/bin/chromedriver"

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_and_retrieve_it_later(self):
        # User first check out the homepage of to-do app
        self.browser.get(self.live_server_url)

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
        self.check_for_row_in_list_table('1: Buy grocery items')
        self.check_for_row_in_list_table('2: Take vegetables')

        self.fail('Finish Test!')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Dixit starts a new todo list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy groceries')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy groceries')

        # He notices that the list has unique URL
        dixit_url = self.browser.current_url
        self.assertRegex(dixit_url, '/lists/.+')

        # Now a new user Shubham come along for new site

        ## We use a new browser session to make sure that no information of
        ## Dixit is comming along from cookies
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Shubham visits the home page there is no sign of Dixit's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy groceries', page_text)

        # Shubham starts new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy milk')

        # Shubham gets his own unique URL
        shubham_url = self.browser.current_url
        self.assertRegex(shubham_url, '/lists/.+')

        # Again there is no trace of Dixit's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy groceries', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied he go back to sleep
