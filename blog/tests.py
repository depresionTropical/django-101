from django.test import TestCase
from .models import Post
# Create your tests here.

class Post_test(TestCase):
    def set_up(self):
        intance = Post.objects.create(title='Curso Django')
        intance.save()
        intance = Post.objects.create(title='Django vs Angular')
        intance.save()

    def test_post(self):
        print(Post.objects.all())
        print(Post.objects.filter(title__icontains='Curso'))