from django.test import TestCase, override_settings

from blog.models import Post

from .models import create_post


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class HomeViewTests(TestCase):
    def test_page_can_be_displayed(self):
        response = self.client.get("/blog/")
        self.assertEqual(response.status_code, 200)
        self.assertInHTML("Latest blogs", str(response.content))


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class BlogsViewTests(TestCase):
    path = "/blog/blogs/"

    def test_5_blogs_rendered_on_page(self):
        for _ in range(5):
            create_post()

        response = self.client.get(self.path)
        actual_number_of_blogs = len(response.context["posts"])
        expected_number_of_blogs = 5

        self.assertEqual(actual_number_of_blogs, expected_number_of_blogs)
        self.assertEqual(response.status_code, 200)

    def test_blogs_sorted_from_newest_to_oldest(self):
        for _ in range(5):
            create_post()

        response = self.client.get(self.path)
        actual_posts = response.context["posts"]

        for i in range(len(actual_posts)):
            try:
                newer_post: Post = actual_posts[i]
                older_post: Post = actual_posts[i + 1]
                self.assertGreater(newer_post.created_at,
                                   older_post.created_at)
            except IndexError:
                print("Index out of range")

        self.assertEqual(response.status_code, 200)


@override_settings(STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage')
class BlogDetailViewTests(TestCase):
    def get_url(self, id):
        return f"/blog/{str(id)}/"

    def test_display_title(self):
        post = create_post()
        response = self.client.get(self.get_url(post.id))
        expected_title = "Blog title 1"
        actual_title = response.context["post"].title

        self.assertEqual(expected_title, actual_title)
