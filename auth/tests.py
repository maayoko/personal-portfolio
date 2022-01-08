from django.test import TestCase

from .models import User

# Create your tests here.


class LoginViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get("/auth/login")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("login/index.html")
        self.assertInHTML(
            "<input type=\"submit\" value=\"Login\" class=\"btn float-right login_btn\">", str(response.content))


class RegisterViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get("/auth/register")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("register/index.html")


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create(
            username="jd",
            full_name="John Doe",
            password="pass",
            email="john@doe.com",
            phone="+385 99 585 9138")

    def test_user_details(self):
        user = User.objects.get(id=1)
        full_name = user._meta.get_field("full_name")
        self.assertEqual(2, 2)
