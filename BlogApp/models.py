from django.db import models

class BlogPost(models.Model):
    blog_cover = models.ImageField(upload_to='blog_covers',null=True)
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_date= models.DateField()
    
class Comments(models.Model):
    owner = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now_add=True)
# Create your models here.




#Template Inheritance
# {% include 'path' %}