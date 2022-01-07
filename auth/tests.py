from django.test import TestCase

# Create your tests here.


class LoginViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("login/index.html")
        self.assertInHTML(
            "<input type=\"submit\" value=\"Login\" class=\"btn float-right login_btn\">", str(response.content))
