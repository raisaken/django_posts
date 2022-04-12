from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published') #super returns the object of parent class or give access to methods/properties of parent class

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    category = models.ForeignKey( 
        Category, on_delete=models.PROTECT, default = 1) #on_delete protect the post on deleting category 
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published') #you can use slug as unique identifier like id
    published = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts') #Cascade: if user is deleted, it also deletes the user's posts
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta: #defines the extra attributes of the model
        ordering = ('-published',)

    def __str__(self): #__str__ represents the string representation of an object
        return self.title


