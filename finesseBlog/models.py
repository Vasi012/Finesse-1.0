from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """Class post for blog posts"""
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        """This class will order the posts"""
        ordering = ["-created_on"]

    def __str__(self):
        """represents the class objects as a string"""
        return self.title

    def number_of_likes(self):
        """Count number of likes"""
        return self.likes.count()


class Comment(models.Model):
    """Add comments and a max_length"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="comments")
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """This class will order the comments"""
        ordering = ["created_on"]

    def __str__(self):
        """represents the class objects as a string"""
        return f"Comment {self.body} by {self.name}"
