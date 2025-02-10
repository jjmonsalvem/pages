# blog/tests.py
from django.urls import reverse
from blog.models import Post


def test_post_createview(self):  # nuevo
    response = self.client.post(
        reverse("post_new"),
        {
            "title": "Nuevo título",
            "body": "Nuevo texto",
            "author": self.user.id,
        },
    )
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Post.objects.last().title, "Nuevo título")
    self.assertEqual(Post.objects.last().body, "Nuevo texto")

def test_post_updateview(self):  # nuevo
    response = self.client.post(
        reverse("post_edit", args="1"),
        {
            "title": "Título actualizado",
            "body": "Texto actualizado",
        },
    )
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Post.objects.last().title, "Título actualizado")
    self.assertEqual(Post.objects.last().body, "Texto actualizado")

def test_post_deleteview(self):  # nuevo
    response = self.client.post(reverse("post_delete", args="1"))
    self.assertEqual(response.status_code, 302)
