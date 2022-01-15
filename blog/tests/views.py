from django.test import TestCase, override_settings


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class HomeViewTests(TestCase):
    def test_page_can_be_displayed(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertInHTML("Latest blogs", str(response.content))
