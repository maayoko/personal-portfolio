from django.test import TestCase, override_settings

from .models import create_post


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class HomeViewTests(TestCase):
    def test_page_can_be_displayed(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertInHTML("Latest blogs", str(response.content))


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class BlogsViewTests(TestCase):
    def test_5_blogs_rendered_on_page(self):
        for _ in range(5):
            create_post()

        response = self.client.get("/blog/blogs/")
        actual_number_of_blogs = len(response.context["posts"])
        expected_number_of_blogs = 5

        self.assertEqual(actual_number_of_blogs, expected_number_of_blogs)
