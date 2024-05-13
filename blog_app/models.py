from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200,null=False)
    image = models.ImageField(upload_to='images/',blank=False,null=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    story = models.TextField()

    def __str__(self):
        return self.title