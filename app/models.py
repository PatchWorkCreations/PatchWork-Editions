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


from django.db import models
from django.contrib.auth.models import User

LANGUAGE_CHOICES = [
    ('sq', 'Albanian'),
    ('am', 'Amharic'),
    ('ar', 'Arabic'),
    ('hy', 'Armenian'),
    ('bn', 'Bengali'),
    ('bs', 'Bosnian'),
    ('bg', 'Bulgarian'),
    ('my', 'Burmese'),
    ('ca', 'Catalan'),
    ('zh', 'Chinese'),
    ('hr', 'Croatian'),
    ('cs', 'Czech'),
    ('da', 'Danish'),
    ('nl', 'Dutch'),
    ('et', 'Estonian'),
    ('fi', 'Finnish'),
    ('fr', 'French'),
    ('ka', 'Georgian'),
    ('de', 'German'),
    ('el', 'Greek'),
    ('gu', 'Gujarati'),
    ('hi', 'Hindi'),
    ('hu', 'Hungarian'),
    ('is', 'Icelandic'),
    ('id', 'Indonesian'),
    ('it', 'Italian'),
    ('ja', 'Japanese'),
    ('kn', 'Kannada'),
    ('kk', 'Kazakh'),
    ('ko', 'Korean'),
    ('lv', 'Latvian'),
    ('lt', 'Lithuanian'),
    ('mk', 'Macedonian'),
    ('ms', 'Malay'),
    ('ml', 'Malayalam'),
    ('mr', 'Marathi'),
    ('mn', 'Mongolian'),
    ('no', 'Norwegian'),
    ('fa', 'Persian'),
    ('pl', 'Polish'),
    ('pt', 'Portuguese'),
    ('pa', 'Punjabi'),
    ('ro', 'Romanian'),
    ('ru', 'Russian'),
    ('sr', 'Serbian'),
    ('sk', 'Slovak'),
    ('sl', 'Slovenian'),
    ('so', 'Somali'),
    ('es', 'Spanish'),
    ('sw', 'Swahili'),
    ('sv', 'Swedish'),
    ('tl', 'Tagalog'),
    ('ta', 'Tamil'),
    ('te', 'Telugu'),
    ('th', 'Thai'),
    ('tr', 'Turkish'),
    ('uk', 'Ukrainian'),
    ('ur', 'Urdu'),
    ('vi', 'Vietnamese'),
    ('en', 'English'),  # fallback/default
]

class SoulThread(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100, blank=True, null=True)
    preferred_mode = models.CharField(max_length=20, default='boss')
    preferred_language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='en')
    last_prompt = models.TextField(blank=True, null=True)
    last_response = models.TextField(blank=True, null=True)
    insights = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SoulThread for {self.user.username}"


from django.db import models
from django.contrib.auth.models import User

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entry = models.TextField()
    mood = models.CharField(max_length=100, blank=True, null=True)  # AI-classified mood
    mood_raw = models.CharField(max_length=255, blank=True, null=True)  # User input
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} – {self.created_at.strftime('%b %d, %Y')}"
