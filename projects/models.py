from django.db import models

# Create your models here.

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    project_url = models.URLField(max_length=200, null=True, blank=True)
    display_order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def technologies_as_list(self):
        return [tech.strip() for tech in self.technology.split(",")]