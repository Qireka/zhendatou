from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(default='')
    background = models.ImageField(default='', upload_to='background')

    def __str__(self):
        return self.name
