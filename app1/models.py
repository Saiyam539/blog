from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumbnail/',default='',blank=True,null=True)
    desc = models.CharField(max_length=100,blank=True,null=True)
    
    heading_1 = models.CharField(max_length=100,blank=True,null=True)
    h1_content = models.CharField(max_length=5000,blank=True,null=True)
    
    heading_2 = models.CharField(max_length=100,blank=True,null=True)
    h2_content = models.CharField(max_length=5000,blank=True,null=True)
    
    heading_3 = models.CharField(max_length=100,blank=True,null=True)
    h3_content = models.CharField(max_length=5000,blank=True,null=True)
    
    heading_4 = models.CharField(max_length=100,blank=True,null=True)
    h4_content = models.CharField(max_length=5000,blank=True,null=True)
    
    code_text = models.CharField(max_length=5000,blank=True,null=True)
    
    content_photo = models.ImageField(upload_to='content_img/',default='',blank=True,null=True)
    ending = models.CharField(max_length=4000,blank=True,null=True)
    publish_date = models.DateField()
    
    
    
    def __str__(self):
        return self.title