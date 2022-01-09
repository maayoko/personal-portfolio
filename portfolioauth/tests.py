from django.test import TestCase
from django.forms.models import model_to_dict

from .models import User

# Create your tests here.


class LoginViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create(
            username="jd",
            full_name="John Doe",
            password="jfdjewdewkjdn",
            email="john@doe.com",
            phone="+385 99 585 9138")

    def test_url_exists(self):
        response = self.client.get("/auth/login")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("login/index.html")
        self.assertInHTML(
            "<input type=\"submit\" value=\"Login\" class=\"btn float-right login_btn\">", str(response.content))

    def test_user_should_login(self):
        user_details = {
            "username": "jd",
            "password": "jfdjewdewkjdn"
        }
        response = self.client.post("/auth/login", user_details)
        self.assertEqual(response.status_code, 302)

    def test_user_do_not_exist(self):
        user_dto = {
            "username": "foo",
            "password": "bar12345678"
        }
        response = self.client.post("/auth/login", user_dto)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("login/index.html")

        string_in_content_idx = str(response.content).find(
            "Wrong email or password")
        self.assertGreater(string_in_content_idx, -1)


class RegisterViewTest(TestCase):
    def test_url_exists(self):
        response = self.client.get("/auth/register")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("register/index.html")

    def test_user_registered(self):
        user = {
            "full_name": "John Doe",
            "username": "jd",
            "password": "fskfkewfkeew",
            "password_1": "fskfkewfkeew",
            "email": "john@doe.com",
            "phone": "+385 99 585 9138"
        }
        response = self.client.post("/auth/register", user)
        self.assertEqual(response.status_code, 302)


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
        username = "jd"
        actual_user = User.objects.get(username=username)
        actual_user = model_to_dict(actual_user)
        expected_user = {
            "full_name": "John Doe",
            "username": "jd",
            "password": "pass",
            "email": "john@doe.com",
            "phone": "+385 99 585 9138"
        }
        self.assertDictContainsSubset(expected_user, actual_user)

    def test_username_should_be_unique(self):
        try:
            User.objects.create(
                username="jd",
                full_name="John Doe",
                password="pass",
                email="john@doe.com",
                phone="+385 99 585 9138")
        except:
            self.assertRaises(RuntimeError)
