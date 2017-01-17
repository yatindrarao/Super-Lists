from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.models import Item

from lists.views import home_page

class HomePageTest(TestCase):
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_only_saves_item_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Second item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item, first_item)
        self.assertEqual(second_saved_item, second_item)


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'lists.html')

    def test_display_all_items(self):
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')

class NewListTest(TestCase):
    def test_can_save_post(self):
        response = self.client.post(
                        '/lists/new',
                        data={'item_text': 'A new list item'}
                    )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        # Checks view renders correct item
        response = self.client.post(
                        '/lists/new',
                        data={'item_text': 'A new list item'}
                    )
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
