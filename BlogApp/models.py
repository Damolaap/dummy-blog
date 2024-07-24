from django.db import models

class BlogPost(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_date= models.DateField()
# Create your models here.




#Template Inheritance
# {% include 'path' %}