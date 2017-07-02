from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    author = models.CharField(max_length=128, blank=True)
    language = models.CharField(max_length=128, blank=True, null=True)
    snippet = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Title: %s\nLanguage: %s\nauthor: %s\nSnippet: %s\nDescription: %s\n" %(self.title, self.language, self.snippet, self.description)
