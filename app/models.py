from django.db import models

# Create your models here.


from django.db import models
from django.urls import reverse

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255, blank=True, null=True)  # Optional for service icons
    order = models.IntegerField(default=0)  # Order for display
    slug = models.SlugField(unique=True)  # For URL routing
    benefits = models.TextField(null=True, blank=True, help_text="Separate each benefit with a new line.")
    how_it_works = models.TextField(null=True, blank=True, help_text="Explain how this service works.")
    image = models.ImageField(upload_to='the_patchwork/images/services/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail', args=[self.slug])


from django.db import models
from django.urls import reverse

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])
    
    def read_time(self):
        word_count = len(self.content.split())
        return f"{word_count // 200} min read"

    def __str__(self):
        return self.title
